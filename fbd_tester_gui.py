"""
FBD Logic Tester - GUI Application
Allows loading .iecfbd files, setting inputs, running test cases,
and comparing actual vs expected outputs for diagnostic purposes.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import json
import os
import sys
import subprocess
import platform
from typing import Dict, Any, List, Optional

# Add current dir to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fbd_simulator import (
    IECFBDParser, FBDSimulator, TestRunner, TestCase,
    Variable, VarType, parse_literal
)

# ─────────────────────────────────────────────
#  Theme
# ─────────────────────────────────────────────
BG = "#1e2230"
BG2 = "#252b3b"
BG3 = "#2d3548"
ACCENT = "#4a9eff"
GREEN = "#2ecc71"
RED = "#e74c3c"
YELLOW = "#f39c12"
FG = "#e8eaf6"
FG2 = "#9ba3c0"
FONT = ("Consolas", 10)
FONT_SM = ("Consolas", 9)
FONT_HDR = ("Segoe UI", 11, "bold")


def styled_label(parent, text, **kw):
    return tk.Label(parent, text=text, bg=kw.pop("bg", BG2),
                    fg=kw.pop("fg", FG), font=kw.pop("font", FONT), **kw)


def styled_button(parent, text, command, color=ACCENT, **kw):
    btn = tk.Button(parent, text=text, command=command,
                    bg=color, fg="white", relief="flat",
                    activebackground=color, activeforeground="white",
                    font=("Segoe UI", 10, "bold"),
                    padx=12, pady=5, cursor="hand2", **kw)
    return btn


def open_in_editor(filepath):
    """Open file in system default editor or Notepad++"""
    if not filepath or not os.path.exists(filepath):
        return False
    
    try:
        # Try to open with Notepad++ first (Windows)
        if platform.system() == "Windows":
            notepadpp_paths = [
                r"C:\Program Files\Notepad++\notepad++.exe",
                r"C:\Program Files (x86)\Notepad++\notepad++.exe",
            ]
            for npp_path in notepadpp_paths:
                if os.path.exists(npp_path):
                    subprocess.Popen([npp_path, filepath])
                    return True
        
        # Fallback to system default editor
        if platform.system() == "Windows":
            os.startfile(filepath)
        elif platform.system() == "Darwin":  # macOS
            subprocess.Popen(["open", filepath])
        else:  # Linux
            subprocess.Popen(["xdg-open", filepath])
        return True
    except Exception as e:
        print(f"Error opening file: {e}")
        return False


# ─────────────────────────────────────────────
#  Input Panel
# ─────────────────────────────────────────────

class VariableInputPanel(tk.Frame):
    """Panel for setting variable input values"""

    def __init__(self, parent, variables: Dict[str, Variable], **kw):
        super().__init__(parent, bg=BG2, **kw)
        self.variables = variables
        self.widgets: Dict[str, tk.Variable] = {}
        self._build()

    def _build(self):
        header = tk.Frame(self, bg=BG3)
        header.pack(fill="x", pady=(0, 2))
        tk.Label(header, text="  Variable", bg=BG3, fg=FG2,
                 font=FONT_SM, width=42, anchor="w").pack(side="left")
        tk.Label(header, text="Type", bg=BG3, fg=FG2,
                 font=FONT_SM, width=8, anchor="w").pack(side="left")
        tk.Label(header, text="Value", bg=BG3, fg=FG2,
                 font=FONT_SM, width=16, anchor="w").pack(side="left")

        canvas = tk.Canvas(self, bg=BG2, highlightthickness=0)
        scroll = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.inner = tk.Frame(canvas, bg=BG2)

        self.inner.bind("<Configure>",
                        lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=self.inner, anchor="nw")
        canvas.configure(yscrollcommand=scroll.set)
        canvas.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

        row = 0
        for name, var in sorted(self.variables.items()):
            bg = BG2 if row % 2 == 0 else BG3
            frame = tk.Frame(self.inner, bg=bg)
            frame.pack(fill="x", pady=1)

            tk.Label(frame, text=f"  {name}", bg=bg, fg=FG,
                     font=FONT_SM, width=42, anchor="w").pack(side="left")
            tk.Label(frame, text=var.var_type.value, bg=bg, fg=FG2,
                     font=FONT_SM, width=8, anchor="w").pack(side="left")

            if var.var_type == VarType.BOOL:
                v = tk.BooleanVar(value=False)
                cb = tk.Checkbutton(frame, variable=v, bg=bg,
                                    activebackground=bg,
                                    selectcolor=BG3, fg=FG)
                cb.pack(side="left")
            else:
                v = tk.StringVar(value="0")
                entry = tk.Entry(frame, textvariable=v, width=14,
                                 bg=BG3, fg=FG, font=FONT_SM,
                                 insertbackground=FG, relief="flat",
                                 bd=2)
                entry.pack(side="left", padx=4)

            self.widgets[name] = v
            row += 1

    def get_values(self) -> Dict[str, Any]:
        result = {}
        for name, widget in self.widgets.items():
            var = self.variables[name]
            raw = widget.get()

            if var.var_type == VarType.BOOL:
                if isinstance(raw, bool):
                    result[name] = raw
                elif isinstance(raw, str):
                    result[name] = raw.lower() in ('true', '1', 'yes', 'on')
                else:
                    result[name] = bool(raw)
            elif var.var_type in (VarType.UINT, VarType.USINT, VarType.INT, VarType.WORD):
                try:
                    result[name] = int(raw)
                except (ValueError, TypeError):
                    result[name] = 0
            elif var.var_type == VarType.REAL:
                try:
                    result[name] = float(raw)
                except (ValueError, TypeError):
                    result[name] = 0.0
            else:
                result[name] = raw
        return result

    def set_values(self, values: Dict[str, Any]):
        for name, val in values.items():
            if name in self.widgets:
                self.widgets[name].set(str(val))


# ─────────────────────────────────────────────
#  Results Panel
# ─────────────────────────────────────────────

class ResultsPanel(tk.Frame):
    def __init__(self, parent, **kw):
        super().__init__(parent, bg=BG2, **kw)
        self._build()

    def _build(self):
        header = tk.Frame(self, bg=BG3)
        header.pack(fill="x")
        for col, w in [("Test Case", 28), ("Status", 8), ("Failures", 50)]:
            tk.Label(header, text=col, bg=BG3, fg=FG2,
                     font=FONT_SM, width=w, anchor="w").pack(side="left", padx=4, pady=4)

        canvas = tk.Canvas(self, bg=BG2, highlightthickness=0)
        scroll = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.inner = tk.Frame(canvas, bg=BG2)
        self.inner.bind("<Configure>",
                        lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=self.inner, anchor="nw")
        canvas.configure(yscrollcommand=scroll.set)
        canvas.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

    def clear(self):
        for w in self.inner.winfo_children():
            w.destroy()

    def add_result(self, test: TestCase):
        bg = BG2 if len(self.inner.winfo_children()) % 2 == 0 else BG3
        frame = tk.Frame(self.inner, bg=bg)
        frame.pack(fill="x", pady=1)

        status_color = GREEN if test.result == "PASS" else RED
        tk.Label(frame, text=test.name, bg=bg, fg=FG,
                 font=FONT_SM, width=28, anchor="w").pack(side="left", padx=4)
        tk.Label(frame, text=test.result, bg=bg, fg=status_color,
                 font=("Consolas", 9, "bold"), width=8, anchor="w").pack(side="left")

        if test.diff:
            fail_text = " | ".join(
                f"{k}: expected={exp!r} actual={act!r}"
                for k, (exp, act) in test.diff.items()
            )
        else:
            fail_text = "All outputs match" if test.result == "PASS" else "-"

        tk.Label(frame, text=fail_text, bg=bg, fg=FG2 if test.result == "PASS" else YELLOW,
                 font=FONT_SM, anchor="w").pack(side="left", padx=4)


# ─────────────────────────────────────────────
#  Live Monitor
# ─────────────────────────────────────────────

class LiveMonitor(tk.Frame):
    """Shows all variable values after simulation"""

    def __init__(self, parent, **kw):
        super().__init__(parent, bg=BG2, **kw)
        self._build()

    def _build(self):
        hdr = tk.Frame(self, bg=BG3)
        hdr.pack(fill="x")
        for text, w in [("Variable", 42), ("Type", 8), ("Value", 20)]:
            tk.Label(hdr, text=text, bg=BG3, fg=FG2,
                     font=FONT_SM, width=w, anchor="w").pack(side="left", padx=3, pady=3)

        canvas = tk.Canvas(self, bg=BG2, highlightthickness=0)
        scroll = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.inner = tk.Frame(canvas, bg=BG2)
        self.inner.bind("<Configure>",
                        lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=self.inner, anchor="nw")
        canvas.configure(yscrollcommand=scroll.set)
        canvas.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")
        self.rows: Dict[str, tk.Label] = {}

    def update_values(self, variables: Dict[str, Variable], outputs: Dict[str, Any]):
        for w in self.inner.winfo_children():
            w.destroy()
        self.rows = {}

        for i, (name, var) in enumerate(sorted(variables.items())):
            bg = BG2 if i % 2 == 0 else BG3
            val = outputs.get(name, var.value)
            frame = tk.Frame(self.inner, bg=bg)
            frame.pack(fill="x", pady=1)

            tk.Label(frame, text=f"  {name}", bg=bg, fg=FG,
                     font=FONT_SM, width=42, anchor="w").pack(side="left")
            tk.Label(frame, text=var.var_type.value, bg=bg, fg=FG2,
                     font=FONT_SM, width=8, anchor="w").pack(side="left")

            val_str = str(val)
            if var.var_type == VarType.BOOL:
                val_color = GREEN if val else RED
                val_str = "TRUE" if val else "FALSE"
            elif isinstance(val, float):
                val_color = ACCENT
            else:
                val_color = FG

            lbl = tk.Label(frame, text=val_str, bg=bg, fg=val_color,
                           font=("Consolas", 9, "bold"), width=20, anchor="w")
            lbl.pack(side="left")
            self.rows[name] = lbl


# ─────────────────────────────────────────────
#  Main Application
# ─────────────────────────────────────────────

class FBDTesterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("FBD Logic Tester — IEC 61131-3 .iecfbd Simulator")
        self.geometry("1400x860")
        self.configure(bg=BG)
        self.resizable(True, True)

        self.parser = IECFBDParser()
        self.simulator: Optional[FBDSimulator] = None
        self.runner: Optional[TestRunner] = None
        self.test_cases: List[TestCase] = []
        self.current_file: str = ""
        self.current_test_file: str = ""

        self.sim_input_panel: Optional[VariableInputPanel] = None
        self.sim_placeholder: Optional[tk.Label] = None
        self.sim_left_frame: Optional[tk.Frame] = None

        self.parsing_window: Optional[tk.Toplevel] = None
        self.test_listbox: Optional[tk.Listbox] = None

        self._apply_styles()
        self._build_ui()

    def _apply_styles(self):
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("TScrollbar", background=BG3, troughcolor=BG2,
                        arrowcolor=FG2, bordercolor=BG3)
        style.configure("TNotebook", background=BG, tabmargins=0)
        style.configure("TNotebook.Tab", background=BG3, foreground=FG,
                        padding=[12, 6], font=("Segoe UI", 10))
        style.map("TNotebook.Tab",
                  background=[("selected", ACCENT)],
                  foreground=[("selected", "white")])

    def _build_ui(self):
        # Top bar
        topbar = tk.Frame(self, bg=BG3, height=52)
        topbar.pack(fill="x")
        topbar.pack_propagate(False)

        # Title section
        title_frame = tk.Frame(topbar, bg=BG3)
        title_frame.pack(side="left", padx=16)
        
        title_label = tk.Label(title_frame, text="⚡ FBD Logic Tester",
                               bg=BG3, fg=FG, font=("Segoe UI", 14, "bold"),
                               cursor="hand2")
        title_label.pack(side="top", anchor="w")
        title_label.bind("<Button-1>", lambda e: self.show_parsing_window())
        
        subtitle_label = tk.Label(title_frame, text="IEC 61131-3 Function Block Diagram Simulator",
                                  bg=BG3, fg=FG2, font=("Segoe UI", 8, "normal"),
                                  cursor="hand2")
        subtitle_label.pack(side="top", anchor="w")
        subtitle_label.bind("<Button-1>", lambda e: self.show_parsing_window())

        self.file_label = tk.Label(topbar, text="No file loaded",
                                   bg=BG3, fg=FG2, font=FONT_SM)
        self.file_label.pack(side="left", padx=20)

        styled_button(topbar, "📂 Open .iecfbd", self.load_file).pack(side="left", padx=6, pady=8)
        styled_button(topbar, "💾 Save Tests", self.save_tests, color="#2980b9").pack(side="left", padx=4)
        styled_button(topbar, "📁 Load Tests", self.load_tests, color="#2980b9").pack(side="left", padx=4)

        self.status_var = tk.StringVar(value="Ready")
        tk.Label(topbar, textvariable=self.status_var,
                 bg=BG3, fg=YELLOW, font=FONT_SM).pack(side="right", padx=16)

        # Main notebook
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=6, pady=6)

        # Tab 1: Manual Simulation
        self.tab_sim = tk.Frame(self.notebook, bg=BG)
        self.notebook.add(self.tab_sim, text="  🔬 Manual Simulation  ")
        self._build_sim_tab(self.tab_sim)

        # Tab 2: Test Cases
        self.tab_tests = tk.Frame(self.notebook, bg=BG)
        self.notebook.add(self.tab_tests, text="  ✅ Test Cases  ")
        self._build_test_tab(self.tab_tests)

    def show_parsing_window(self):
        """Open a separate window showing parsed FBD logic"""
        if not self.simulator:
            messagebox.showinfo("Info", "Najpierw wczytaj plik .iecfbd aby zobaczyć sparsowaną logikę.")
            return
        
        if self.parsing_window and self.parsing_window.winfo_exists():
            self.parsing_window.lift()
            self.parsing_window.focus_force()
            return
        
        self.parsing_window = tk.Toplevel(self)
        self.parsing_window.title("Parsing - Podgląd sparsowanej logiki FBD")
        self.parsing_window.geometry("1000x700")
        self.parsing_window.configure(bg=BG)
        self.parsing_window.transient(self)
        
        self._build_parsing_window(self.parsing_window)
        
        if hasattr(self, 'simulator') and self.simulator:
            self._populate_parsing_view(self.parsing_window)
        
        self.parsing_window.protocol("WM_DELETE_WINDOW", self._close_parsing_window)
    
    def _close_parsing_window(self):
        if self.parsing_window:
            self.parsing_window.destroy()
            self.parsing_window = None
    
    def _build_parsing_window(self, parent):
        explanation_frame = tk.Frame(parent, bg=ACCENT, height=120)
        explanation_frame.pack(fill="x", padx=10, pady=(10, 5))
        explanation_frame.pack_propagate(False)
        
        explanation_text = tk.Text(explanation_frame, bg=ACCENT, fg="white",
                                   font=("Segoe UI", 10), wrap="word",
                                   relief="flat", bd=0, padx=15, pady=10)
        explanation_text.pack(fill="both", expand=True)
        
        explanation = """📖 Co widzisz w tym oknie?
        
To jest podgląd sparsowanej logiki z pliku .iecfbd. Po wczytaniu pliku, parser analizuje jego strukturę 
i wyodrębnia sieci logiczne (Networks) wraz z instrukcjami.

Każda sieć reprezentuje fragment logiki sterowania, który będzie symulowany przez silnik FBD.

• Network X - numer sieci logicznej
• Instrukcje - poszczególne operacje w sieci (przypisania, wywołania bloków funkcyjnych)

Ta informacja jest pomocna przy debugowaniu i zrozumieniu, jak parser zinterpretował twój plik."""
        
        explanation_text.insert("1.0", explanation)
        explanation_text.config(state="disabled")
        
        separator = ttk.Separator(parent, orient='horizontal')
        separator.pack(fill='x', padx=10, pady=5)
        
        logic_frame = tk.Frame(parent, bg=BG)
        logic_frame.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        
        tk.Label(logic_frame, text="SPARSOWANA LOGIKA FBD",
                 bg=BG3, fg=FG2, font=FONT_HDR, pady=6).pack(fill="x")
        
        self.parsing_text = scrolledtext.ScrolledText(
            logic_frame, bg=BG2, fg=FG, font=("Consolas", 10),
            insertbackground=FG, relief="flat", bd=0,
            wrap="none"
        )
        self.parsing_text.pack(fill="both", expand=True)
        self.parsing_text.config(state="disabled")
    
    def _populate_parsing_view(self, parent_window=None):
        if not hasattr(self, 'simulator') or not self.simulator:
            return
        
        if parent_window and hasattr(self, 'parsing_text') and self.parsing_text.winfo_exists():
            text_widget = self.parsing_text
        else:
            return
        
        text_widget.config(state="normal")
        text_widget.delete("1.0", "end")
        
        networks = self.simulator.networks
        
        if not networks:
            text_widget.insert("end", "// No networks found in the file.\n")
        else:
            for net in networks:
                text_widget.insert("end", f"// ═══════════════════════════════════════\n")
                text_widget.insert("end", f"// Network {net.number}:\n")
                text_widget.insert("end", f"// ═══════════════════════════════════════\n")
                for instr in net.instructions:
                    text_widget.insert("end", f"    {instr}\n")
                text_widget.insert("end", "\n")
        
        text_widget.config(state="disabled")

    def _build_sim_tab(self, parent):
        pane = tk.PanedWindow(parent, orient="horizontal", bg=BG,
                              sashwidth=4)
        pane.pack(fill="both", expand=True, padx=6, pady=6)

        self.sim_left_frame = tk.Frame(pane, bg=BG)
        pane.add(self.sim_left_frame, width=460)

        hdr_l = tk.Frame(self.sim_left_frame, bg=ACCENT)
        hdr_l.pack(fill="x")
        tk.Label(hdr_l, text="  INPUT VARIABLES", bg=ACCENT, fg="white",
                 font=FONT_HDR, pady=6).pack(side="left")

        self.sim_placeholder = tk.Label(self.sim_left_frame,
                                        text="Load a .iecfbd file to begin",
                                        bg=BG2, fg=FG2, font=("Segoe UI", 12))
        self.sim_placeholder.pack(fill="both", expand=True)

        btn_frame = tk.Frame(self.sim_left_frame, bg=BG, pady=6)
        btn_frame.pack(fill="x")
        styled_button(btn_frame, "▶  Run Cycle", self.run_simulation,
                      color=GREEN).pack(side="left", padx=6)
        styled_button(btn_frame, "↺  Reset", self.reset_simulation,
                      color="#555").pack(side="left", padx=4)

        right = tk.Frame(pane, bg=BG)
        pane.add(right)

        hdr_r = tk.Frame(right, bg="#7b52ab")
        hdr_r.pack(fill="x")
        tk.Label(hdr_r, text="  OUTPUT MONITOR", bg="#7b52ab", fg="white",
                 font=FONT_HDR, pady=6).pack(side="left")

        self.live_monitor = LiveMonitor(right)
        self.live_monitor.pack(fill="both", expand=True)

    def _build_test_tab(self, parent):
        left = tk.Frame(parent, bg=BG)
        left.pack(side="left", fill="y", padx=(6, 0), pady=6)
        
        tk.Label(left, text="TEST CASES", bg=BG3, fg=FG2,
                 font=FONT_HDR, pady=6).pack(fill="x")

        listbox_frame = tk.Frame(left, bg=BG2)
        listbox_frame.pack(fill="both", expand=True, pady=4)
        
        scrollbar = ttk.Scrollbar(listbox_frame, orient="vertical")
        self.test_listbox = tk.Listbox(listbox_frame, bg=BG2, fg=FG, font=FONT,
                                       selectbackground=ACCENT,
                                       relief="flat", bd=0,
                                       activestyle="none",
                                       width=32,
                                       yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.test_listbox.yview)
        
        self.test_listbox.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        btns = tk.Frame(left, bg=BG)
        btns.pack(fill="x", pady=(5, 0))
        
        btn_edit = styled_button(btns, "✎ Edit", self.edit_test_case, color=GREEN)
        btn_edit.pack(side="left", padx=2, pady=4, fill="x", expand=True)
        
        btn_del = styled_button(btns, "✗ Del", self.delete_test_case, color=RED)
        btn_del.pack(side="left", padx=2, pady=4, fill="x", expand=True)
        
        btn_run = styled_button(btns, "▶ Run All", self.run_all_tests, color=ACCENT)
        btn_run.pack(side="left", padx=2, pady=4, fill="x", expand=True)

        right = tk.Frame(parent, bg=BG)
        right.pack(side="left", fill="both", expand=True, padx=6, pady=6)

        self.summary_frame = tk.Frame(right, bg=BG3, pady=8)
        self.summary_frame.pack(fill="x")
        self.summary_label = tk.Label(self.summary_frame,
                                      text="Run tests to see results",
                                      bg=BG3, fg=FG2, font=FONT_HDR)
        self.summary_label.pack()

        tk.Label(right, text="TEST RESULTS", bg=BG3, fg=FG2,
                 font=FONT_HDR, pady=6).pack(fill="x")
        self.results_panel = ResultsPanel(right)
        self.results_panel.pack(fill="both", expand=True)

    def load_file(self, filepath: str = ""):
        if not filepath:
            filepath = filedialog.askopenfilename(
                title="Open .iecfbd file",
                filetypes=[("IEC FBD files", "*.iecfbd"), ("All files", "*.*")]
            )
        if not filepath:
            return

        try:
            fb_name, variables, networks = self.parser.parse(filepath)
            self.simulator = FBDSimulator(fb_name, variables, networks)
            self.runner = TestRunner(self.simulator)
            self.current_file = filepath

            fname = os.path.basename(filepath)
            self.file_label.config(text=f"📄 {fname}  [{fb_name}]  —  "
                                        f"{len(variables)} vars, {len(networks)} networks")
            self.status_var.set(f"Loaded: {fb_name}")

            self._rebuild_sim_tab_inputs(variables)
            
            if self.parsing_window and self.parsing_window.winfo_exists():
                self._populate_parsing_view(self.parsing_window)

        except Exception as ex:
            messagebox.showerror("Parse Error", f"Failed to load file:\n{ex}")
            import traceback
            traceback.print_exc()

    def _rebuild_sim_tab_inputs(self, variables):
        if not self.sim_left_frame:
            return

        if self.sim_placeholder and self.sim_placeholder.winfo_exists():
            self.sim_placeholder.destroy()
            self.sim_placeholder = None

        if self.sim_input_panel and self.sim_input_panel.winfo_exists():
            self.sim_input_panel.destroy()

        btn_frame = None
        for child in self.sim_left_frame.winfo_children():
            if isinstance(child, tk.Frame) and any(
                    isinstance(grandchild, tk.Button) for grandchild in child.winfo_children()):
                btn_frame = child
                break

        self.sim_input_panel = VariableInputPanel(self.sim_left_frame, variables)

        if btn_frame:
            self.sim_input_panel.pack(fill="both", expand=True, before=btn_frame)
        else:
            self.sim_input_panel.pack(fill="both", expand=True)

    def run_simulation(self):
        if not self.simulator or not self.sim_input_panel:
            messagebox.showwarning("No file", "Please load a .iecfbd file first.")
            return
        inputs = self.sim_input_panel.get_values()
        self.simulator.set_inputs(inputs)
        outputs = self.simulator.execute_cycle()
        self.live_monitor.update_values(self.simulator.variables, outputs)
        self.status_var.set("Simulation cycle complete")

    def reset_simulation(self):
        if self.simulator:
            self.simulator.reset()
            self.live_monitor.update_values(self.simulator.variables, {})
            self.status_var.set("Simulation reset")

    def edit_test_case(self):
        """Edit test cases - opens JSON file in external editor"""
        if not self.simulator:
            messagebox.showwarning("No file", "Please load a .iecfbd file first.")
            return
        
        filepath = filedialog.askopenfilename(
            title="Select test cases JSON file to edit",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if not filepath:
            return
        
        self.current_test_file = filepath
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            self.test_cases.clear()
            if self.test_listbox:
                self.test_listbox.delete(0, "end")
            
            for item in data:
                def coerce(val_str, varname):
                    var = self.simulator.variables.get(varname)
                    if var is None:
                        return val_str
                    if var.var_type == VarType.BOOL:
                        return str(val_str).lower() in ("true", "1", "yes")
                    if var.var_type in (VarType.UINT, VarType.USINT, VarType.INT):
                        try:
                            return int(val_str)
                        except ValueError:
                            return 0
                    if var.var_type == VarType.REAL:
                        try:
                            return float(val_str)
                        except ValueError:
                            return 0.0
                    return val_str                
                inputs = {k: coerce(v, k) for k, v in item.get("inputs", {}).items()}
                outputs = {k: coerce(v, k) for k, v in item.get("expected_outputs", {}).items()}
                tc = TestCase(name=item.get("name", "Unknown"),
                              description=item.get("description", ""),
                              inputs=inputs, expected_outputs=outputs)
                self.test_cases.append(tc)
                if self.test_listbox:
                    self.test_listbox.insert("end", tc.name)
            
            self.status_var.set(f"Loaded {len(self.test_cases)} test cases from {os.path.basename(filepath)}")
            
            if open_in_editor(filepath):
                self.status_var.set(f"Opened {os.path.basename(filepath)} in editor")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {e}")

    def _save_tests_to_file(self):
        """Save current test cases to the current JSON file"""
        if not self.current_test_file:
            path = filedialog.asksaveasfilename(
                title="Save test cases",
                defaultextension=".json",
                filetypes=[("JSON", "*.json")]
            )
            if not path:
                return
            self.current_test_file = path
        
        data = [{
            "name": tc.name,
            "description": tc.description,
            "inputs": {k: str(v) for k, v in tc.inputs.items()},
            "expected_outputs": {k: str(v) for k, v in tc.expected_outputs.items()},
        } for tc in self.test_cases]
        
        with open(self.current_test_file, "w", encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def delete_test_case(self):
        """Delete selected test case"""
        if not self.test_listbox:
            return
            
        selection = self.test_listbox.curselection()
        if not selection:
            messagebox.showwarning("No selection", "Please select a test case to delete.")
            return
            
        idx = selection[0]
        if idx >= len(self.test_cases):
            return
            
        test_name = self.test_cases[idx].name
        
        if messagebox.askyesno("Confirm Delete", f"Delete test case '{test_name}'?"):
            self.test_cases.pop(idx)
            self.test_listbox.delete(idx)
            if self.current_test_file:
                self._save_tests_to_file()
            self.status_var.set(f"Deleted test case: {test_name}")

    def run_all_tests(self):
        """Run all test cases"""
        if not self.runner:
            messagebox.showwarning("No file", "Please load a .iecfbd file first.")
            return
            
        if not self.test_cases:
            messagebox.showwarning("No tests", "Load test cases first.")
            return

        self.runner.results.clear()
        self.results_panel.clear()

        for tc in self.test_cases:
            result = self.runner.run(tc)
            self.results_panel.add_result(result)

        summary = self.runner.summary()
        color = GREEN if summary["failed"] == 0 else RED
        text = f"  {summary['passed']}/{summary['total']} PASSED  | {summary['failed']} FAILED"
        self.summary_label.config(text=text, fg=color)
        self.status_var.set(f"Tests: {summary['passed']}/{summary['total']} passed")

    def save_tests(self):
        """Save tests to JSON file"""
        if not self.test_cases:
            messagebox.showinfo("Empty", "No test cases to save.")
            return
        
        self._save_tests_to_file()
        messagebox.showinfo("Saved", f"Saved {len(self.test_cases)} test cases to {os.path.basename(self.current_test_file)}")

    def load_tests(self):
        """Load tests from JSON file"""
        if not self.simulator:
            messagebox.showwarning("No file", "Please load a .iecfbd file first.")
            return
        
        path = filedialog.askopenfilename(
            title="Load test cases",
            filetypes=[("JSON", "*.json")]
        )
        if not path:
            return

        try:
            with open(path, "r", encoding='utf-8') as f:
                data = json.load(f)

            self.test_cases.clear()
            if self.test_listbox:
                self.test_listbox.delete(0, "end")

            for item in data:
                def coerce(val_str, varname):
                    var = self.simulator.variables.get(varname)
                    if var is None:
                        return val_str
                    if var.var_type == VarType.BOOL:
                        return str(val_str).lower() in ("true", "1", "yes")
                    if var.var_type in (VarType.UINT, VarType.USINT, VarType.INT):
                        try:
                            return int(val_str)
                        except ValueError:
                            return 0
                    if var.var_type == VarType.REAL:
                        try:
                            return float(val_str)
                        except ValueError:
                            return 0.0
                    return val_str

                inputs = {k: coerce(v, k) for k, v in item.get("inputs", {}).items()}
                outputs = {k: coerce(v, k) for k, v in item.get("expected_outputs", {}).items()}
                tc = TestCase(name=item.get("name", "Unknown"),
                              description=item.get("description", ""),
                              inputs=inputs, expected_outputs=outputs)
                self.test_cases.append(tc)
                if self.test_listbox:
                    self.test_listbox.insert("end", tc.name)

            self.current_test_file = path
            self.status_var.set(f"Loaded {len(self.test_cases)} test cases from {os.path.basename(path)}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load tests: {e}")


# ─────────────────────────────────────────────
#  Entry point
# ─────────────────────────────────────────────

def main():
    app = FBDTesterApp()

    # Auto-load file passed as argument
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        app.after(200, lambda: app.load_file(sys.argv[1]))

    app.mainloop()


if __name__ == "__main__":
    main()
