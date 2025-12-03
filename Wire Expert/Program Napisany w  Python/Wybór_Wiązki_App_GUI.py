# import customtkinter as ctk
# import tkinter as tk
# from tkinter import messagebox
#
# # ====================================================================
# # I. PEŁNE MAPOWANIA DANYCH (Bez zmian)
# # ====================================================================
#
# MAPOWANIE_ORIENTACJI_DO_WYBORU = {'85': 'Proste (Straight)', '84': 'Kątowe (Angled)'}
# MAPOWANIE_KABLA = {'00': 'Brak Kabla', '05': 'RG58', '06': 'RG174', '07': 'H155'}
# MAPOWANIE_ZLACZY_T1 = {
#     '000': 'Brak Złącza', '100': 'FAKRA Cod. E (F)', '101': 'FAKRA Cod. E (M)', '102': 'FME (F)', '103': 'FME (M)',
#     '104': 'BNC (F)', '105': 'BNC (M)', '106': 'SMA (F)', '107': 'SMA (M)', '108': 'R-SMA (F)',
#     '109': 'R-SMA (M)', '110': 'SMB (F)', '111': 'SMB (M)', '112': 'UHF (F)', '113': 'UHF (M)',
#     '114': 'mini UHF (F)', '115': 'mini UHF (M)', '116': 'FAKRA Cod. A (F)', '117': 'FAKRA Cod. A (M)',
#     '118': 'FAKRA Cod. B (F)', '119': 'FAKRA Cod. B (M)', '120': 'FAKRA Cod. C (F)', '121': 'FAKRA Cod. C (M)',
#     '122': 'FAKRA Cod. D (F)', '123': 'FAKRA Cod. D (M)', '124': 'FAKRA Cod. M (F)', '125': 'FAKRA Cod. M (M)',
#     '126': 'FAKRA Cod. N (F)', '127': 'FAKRA Cod. N (M)', '128': 'FAKRA Cod. Z (F)', '129': 'FAKRA Cod. Z (M)',
#     '130': 'M10 (F)', '131': 'M10 (M)', '132': 'FAKRA Cod. F (F)', '133': 'FAKRA Cod. F (M)',
#     '134': 'FAKRA Cod. G (F)', '135': 'FAKRA Cod. G (M)', '136': 'FAKRA Cod. H (F)', '137': 'FAKRA Cod. H (M)',
#     '138': 'FAKRA Cod. I (F)', '139': 'FAKRA Cod. I (M)', '140': 'FAKRA Cod. K (F)', '141': 'FAKRA Cod. K (M)',
#     '142': 'FAKRA Cod. L (F)', '143': 'FAKRA Cod. L (M)',
# }
# MAPOWANIE_ZLACZY_T2 = {
#     '000': 'Brak Złącza', '500': 'FAKRA Cod. M (F)', '501': 'FAKRA Cod. M (M)', '502': 'FAKRA Cod. N (F)',
#     '503': 'FAKRA Cod. N (M)', '504': 'FAKRA Cod. Z (F)', '505': 'FAKRA Cod. Z (M)', '506': 'M10 (F)',
#     '507': 'M10 (M)', '508': 'FAKRA Cod. F (F)', '509': 'FAKRA Cod. F (M)', '510': 'FAKRA Cod. G (F)',
#     '511': 'FAKRA Cod. G (M)', '512': 'FAKRA Cod. H (F)', '513': 'FAKRA Cod. H (M)', '514': 'FAKRA Cod. I (F)',
#     '515': 'FAKRA Cod. I (M)', '516': 'FAKRA Cod. K (F)', '517': 'FAKRA Cod. K (M)', '518': 'FAKRA Cod. L (F)',
#     '519': 'FAKRA Cod. L (M)', '520': 'mini UHF (F)', '521': 'mini UHF (M)', '522': 'FAKRA Cod. A (F)',
#     '523': 'FAKRA Cod. A (M)', '524': 'FAKRA Cod. B (F)', '525': 'FAKRA Cod. B (M)', '526': 'FAKRA Cod. C (F)',
#     '527': 'FAKRA Cod. C (M)', '528': 'FAKRA Cod. D (F)', '529': 'FAKRA Cod. D (M)', '530': 'FAKRA Cod. E (F)',
#     '531': 'FAKRA Cod. E (M)', '532': 'FME (F)', '533': 'FME (M)', '534': 'BNC (F)', '535': 'BNC (M)',
#     '536': 'SMA (F)', '537': 'SMA (M)', '538': 'R-SMA (F)', '539': 'R-SMA (M)', '540': 'SMB (F)',
#     '541': 'SMB (M)', '542': 'UHF (F)', '543': 'UHF (M)',
# }
# MAPOWANIE_DLUGOSCI = {
#     '030': '3.0 m', '035': '3.5 m', '040': '4.0 m', '045': '4.5 m',
#     '050': '5.0 m', '055': '5.5 m', '060': '6.0 m', '065': '6.5 m',
#     '070': '7.0 m', '075': '7.5 m', '080': '8.0 m', '085': '8.5 m',
#     '090': '9.0 m', '095': '9.5 m', '100': '10.0 m', '105': '10.5 m',
#     '110': '11.0 m'
# }
#
#
# # Funkcja pomocnicza do zamiany klucz-wartość na listę wartości
# def get_map_values(mapping):
#     return list(mapping.values())
#
#
# # Funkcja pomocnicza do znalezienia klucza po wartości
# def get_key_by_value(mapping, value):
#     for key, val in mapping.items():
#         if val == value:
#             return key
#     return None
#
#
# # ====================================================================
# # II. KLASA GENERATORA Z CUSTOMTKINTER
# # ====================================================================
#
# # DEFINE KEY COLORS FOR MODERN LOOK
# ACCENT_COLOR = "#008080"  # Ciemny Teal/Cyjan - Elegancki akcent
# HOVER_COLOR = "#005a5a"  # Ciemniejszy odcień dla hovera
# MAIN_BG = "gray90"  # Bardzo jasne tło
# CARD_BG = "white"  # Czysta biel dla kart/widżetów
# TEXT_COLOR = "gray20"  # Miękka czerń dla tekstu
#
#
# class GeneratorKabliApp(ctk.CTk):
#     def __init__(self):
#         super().__init__()
#
#         # DEFINICJE CZCIONEK
#         self.GLOBAL_FONT = ctk.CTkFont(family="Arial", size=13)
#         self.GLOBAL_FONT_BOLD = ctk.CTkFont(family="Arial", size=14, weight="bold")
#
#         self.title("Generator Numerów Katalogowych Kabli (Modern UI)")
#         self.geometry("1000x700")
#         self.config(bg=MAIN_BG)  # Ustawienie tła głównego okna
#         self.grid_columnconfigure(0, weight=1)
#         self.grid_rowconfigure(0, weight=1)
#
#         # Ustawienia wyglądu
#         ctk.set_appearance_mode("Light")
#         ctk.set_default_color_theme("blue")  # Możemy użyć blue theme jako bazy
#
#         self.mapy = {
#             'T1': MAPOWANIE_ZLACZY_T1, 'T2': MAPOWANIE_ZLACZY_T2,
#             'O': MAPOWANIE_ORIENTACJI_DO_WYBORU, 'K': MAPOWANIE_KABLA, 'D': MAPOWANIE_DLUGOSCI
#         }
#
#         self.kod_t1 = tk.StringVar(value=get_map_values(self.mapy['T1'])[0])
#         self.kod_o1 = tk.StringVar(value=get_map_values(self.mapy['O'])[0])
#         self.kod_t2 = tk.StringVar(value=get_map_values(self.mapy['T2'])[0])
#         self.kod_o2 = tk.StringVar(value=get_map_values(self.mapy['O'])[0])
#         self.kod_k = tk.StringVar(value=get_map_values(self.mapy['K'])[0])
#         self.kod_d = tk.StringVar(value=get_map_values(self.mapy['D'])[0])
#
#         self.menu_t1_ref = None
#         self.menu_t2_ref = None
#         self.menu_o1_ref = None
#         self.menu_o2_ref = None
#         self.menu_k_ref = None
#         self.menu_d_ref = None
#
#         self.utworz_interfejs()
#         self.bind_events()
#         self.aktualizuj_stan_gui()
#         self.generuj_numer_katalogowy()
#
#     def utworz_interfejs(self):
#         # 🌟 Zastosowanie tła głównego
#         main_frame = ctk.CTkFrame(self, corner_radius=10, fg_color=MAIN_BG)
#         main_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
#
#         main_frame.grid_columnconfigure((0, 2), weight=3)
#         main_frame.grid_columnconfigure((1, 3), weight=1)
#
#         # 1. Złącza T1 i T2 (Szersze)
#         self.menu_t1_ref = self.tworz_sekcje_wyboru(main_frame, "1. Złącze T1 (3c) 🔌", self.mapy['T1'], self.kod_t1, 0,
#                                                     0, wide=True)
#         self.menu_t2_ref = self.tworz_sekcje_wyboru(main_frame, "2. Złącze T2 (3c) 🔌", self.mapy['T2'], self.kod_t2, 0,
#                                                     2, wide=True)
#
#         # 2. Orientacje O1 i O2 (Węższe)
#         self.menu_o1_ref = self.tworz_sekcje_wyboru(main_frame, "3. Orientacja O1 (2c) 📐", self.mapy['O'], self.kod_o1,
#                                                     2, 0, wide=False)
#         self.menu_o2_ref = self.tworz_sekcje_wyboru(main_frame, "4. Orientacja O2 (2c) 📐", self.mapy['O'], self.kod_o2,
#                                                     2, 2, wide=False)
#
#         # 3. Kabel i Długość (Średnie)
#         self.menu_k_ref = self.tworz_sekcje_wyboru(main_frame, "5. Typ Kabla K (2c) 🧵", self.mapy['K'], self.kod_k, 4,
#                                                    0, wide=False)
#         self.menu_d_ref = self.tworz_sekcje_wyboru(main_frame, "6. Długość Kabla D (3c) 📏", self.mapy['D'], self.kod_d,
#                                                    4, 2, wide=False)
#
#         ctk.CTkLabel(main_frame, text="", height=20, fg_color=MAIN_BG).grid(row=6, columnspan=4, sticky="ew")
#
#         # --- SEKCJA WYNIKU I PRZYCISK (Dół - Pasek Stanu) ---
#
#         # 🌟 Wynik w "chipie" na dole
#         result_frame = ctk.CTkFrame(main_frame, fg_color=CARD_BG, corner_radius=10, border_color="gray70",
#                                     border_width=1)
#         result_frame.grid(row=7, column=0, columnspan=4, sticky="ew", padx=10, pady=10)
#         result_frame.grid_columnconfigure(0, weight=4)
#         result_frame.grid_columnconfigure(1, weight=1)
#
#         ctk.CTkLabel(result_frame, text="NUMER KATALOGOWY:", font=self.GLOBAL_FONT_BOLD, text_color=TEXT_COLOR).grid(
#             row=0, column=0, sticky='w', padx=15, pady=(10, 0))
#
#         self.wynik_label = ctk.CTkLabel(result_frame, text="---", font=ctk.CTkFont(size=26, weight="bold"),
#                                         text_color=ACCENT_COLOR)
#         self.wynik_label.grid(row=1, column=0, sticky='w', padx=15, pady=(0, 10))
#
#         # 🌟 Elegancki przycisk akcji
#         ctk.CTkButton(result_frame, text="ZAMAWIAM",
#                       command=lambda: self.generuj_numer_katalogowy(pokaz_alert=True),
#                       font=ctk.CTkFont(size=14, weight="bold"),
#                       height=50,
#                       fg_color=ACCENT_COLOR,
#                       hover_color=HOVER_COLOR
#                       ).grid(row=0, column=1, rowspan=2, sticky='e', padx=15, pady=10)
#
#         for i in [1, 3, 5]:
#             main_frame.grid_rowconfigure(i, weight=1)
#
#         return main_frame
#
#     def tworz_sekcje_wyboru(self, frame, label_text, mapa_danych, ctk_variable, start_row, start_column, wide=False):
#         """Tworzy sekcję wyboru (Modern Card UI) z użyciem CTkOptionMenu."""
#
#         # 🌟 Karta w czystej bieli z delikatną ramką
#         card_frame = ctk.CTkFrame(frame, fg_color=CARD_BG, corner_radius=10, border_color="gray80", border_width=1)
#         span = 2 if wide else 1
#         card_frame.grid(row=start_row, column=start_column, columnspan=span,
#                         rowspan=2, sticky="nsew", padx=10, pady=10)
#         card_frame.grid_columnconfigure(0, weight=1)
#
#         # Tytuł karty
#         ctk.CTkLabel(card_frame, text=label_text,
#                      font=self.GLOBAL_FONT_BOLD, text_color=ACCENT_COLOR  # Kolor akcentu na nagłówku
#                      ).grid(row=0, column=0, sticky='w', padx=15, pady=(15, 5))
#
#         menu_width = 300 if wide else 180
#
#         # 🌟 OptionMenu z płaską, białą stylizacją
#         option_menu = ctk.CTkOptionMenu(
#             card_frame,
#             values=get_map_values(mapa_danych),
#             command=self.on_selection_change,
#             variable=ctk_variable,
#             font=self.GLOBAL_FONT,
#             text_color=TEXT_COLOR,
#
#             # Wpływa na wygląd listy rozwijanej (dopasowanie do białego tła)
#             dropdown_font=self.GLOBAL_FONT,
#             dropdown_text_color=TEXT_COLOR,
#             dropdown_fg_color="gray95",  # Subtelne tło listy
#             dropdown_hover_color="gray85",  # Bardzo subtelny hover
#
#             # Stylizacja widoku zamkniętego (OptionMenu)
#             fg_color="gray95",  # Bardzo jasne tło widżetu głównego, aby nadać mu "cienia"
#             button_color=ACCENT_COLOR,  # Przycisk akcentujący
#             button_hover_color=HOVER_COLOR,
#
#             width=menu_width,
#             height=35
#
#         )
#         option_menu.grid(row=1, column=0, sticky='ew', padx=15, pady=(0, 15))
#
#         return option_menu
#
#     def bind_events(self):
#         self.kod_t1.trace_add("write", lambda *args: self.on_selection_change(self.kod_t1.get()))
#         self.kod_o1.trace_add("write", lambda *args: self.on_selection_change(self.kod_o1.get()))
#         self.kod_t2.trace_add("write", lambda *args: self.on_selection_change(self.kod_t2.get()))
#         self.kod_o2.trace_add("write", lambda *args: self.on_selection_change(self.kod_o2.get()))
#         self.kod_k.trace_add("write", lambda *args: self.on_selection_change(self.kod_k.get()))
#         self.kod_d.trace_add("write", lambda *args: self.on_selection_change(self.kod_d.get()))
#
#     def on_selection_change(self, value):
#         self.aktualizuj_stan_gui()
#         self.generuj_numer_katalogowy()
#
#     def aktualizuj_stan_gui(self):
#         t1_val = get_key_by_value(self.mapy['T1'], self.kod_t1.get())
#         t2_val = get_key_by_value(self.mapy['T2'], self.kod_t2.get())
#         k_val = get_key_by_value(self.mapy['K'], self.kod_k.get())
#
#         self._toggle_menu_state(self.menu_o1_ref, 'O1', t1_val != '000', self.kod_o1, self.mapy['O'])
#         self._toggle_menu_state(self.menu_o2_ref, 'O2', t2_val != '000', self.kod_o2, self.mapy['O'])
#         self._toggle_menu_state(self.menu_d_ref, 'D', k_val != '00', self.kod_d, self.mapy['D'])
#
#     def _toggle_menu_state(self, menu, name, should_enable, variable, default_map):
#         if should_enable:
#             menu.configure(state="normal")
#             menu.configure(values=get_map_values(default_map))
#             if variable.get() == f"--- POMINIĘTE {name} ---":
#                 new_value = get_map_values(default_map)[0]
#                 variable.set(new_value)
#                 menu.set(new_value)
#         else:
#             menu.configure(state="disabled")
#             disabled_value = f"--- POMINIĘTE {name} ---"
#             variable.set(disabled_value)
#             menu.configure(values=[disabled_value])
#             menu.set(disabled_value)
#
#     def generuj_numer_katalogowy(self, pokaz_alert=False):
#         T1 = get_key_by_value(self.mapy['T1'], self.kod_t1.get())
#         O1 = get_key_by_value(self.mapy['O'], self.kod_o1.get())
#         T2 = get_key_by_value(self.mapy['T2'], self.kod_t2.get())
#         O2 = get_key_by_value(self.mapy['O'], self.kod_o2.get())
#         K = get_key_by_value(self.mapy['K'], self.kod_k.get())
#         D = get_key_by_value(self.mapy['D'], self.kod_d.get())
#
#         segmenty = []
#
#         wszystko_ok = True
#
#         if T1 is not None:
#             segmenty.append(T1)
#             if T1 != '000':
#                 if O1 is None:
#                     wszystko_ok = False
#                 elif 'POMINIĘTE' not in self.kod_o1.get():
#                     segmenty.append(O1)
#
#         if T2 is not None:
#             segmenty.append(T2)
#             if T2 != '000':
#                 if O2 is None:
#                     wszystko_ok = False
#                 elif 'POMINIĘTE' not in self.kod_o2.get():
#                     segmenty.append(O2)
#
#         if K is not None:
#             segmenty.append(K)
#             if K != '00':
#                 if D is None:
#                     wszystko_ok = False
#                 elif 'POMINIĘTE' not in self.kod_d.get():
#                     segmenty.append(D)
#
#         numer_katalogowy = "".join(segmenty)
#         dlugosc_numeru = len(numer_katalogowy)
#
#         if numer_katalogowy and wszystko_ok:
#             self.wynik_label.configure(text=f"{numer_katalogowy} ({dlugosc_numeru} cyfr)", text_color=ACCENT_COLOR)
#         else:
#             self.wynik_label.configure(text="--- BRAK DANYCH (BŁĄD) ---", text_color="#e74c3c")
#
#         if pokaz_alert and wszystko_ok and numer_katalogowy:
#             messagebox.showinfo("Potwierdzenie Zamówienia",
#                                 f"Złożono zamówienie na produkt:\n{numer_katalogowy}\nDługość kodu: {dlugosc_numeru} cyfr")
#         elif pokaz_alert and not wszystko_ok:
#             messagebox.showerror("Błąd Weryfikacji",
#                                  "Nie wybrano wymaganych orientacji/długości. Proszę sprawdzić wszystkie aktywne pola.")
#
#
# # ====================================================================
# # III. URUCHOMIENIE APLIKACJI
# # ====================================================================
#
# if __name__ == "__main__":
#     app = GeneratorKabliApp()
#     app.mainloop()

#-----------------------------------------------------------------------------------------------------------------------

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import sys

# ====================================================================
# I. PEŁNE MAPOWANIA DANYCH (Bez zmian)
# ====================================================================

MAPOWANIE_ORIENTACJI_DO_WYBORU = {'85': 'Proste (Straight)', '84': 'Kątowe (Angled)'}
MAPOWANIE_KABLA = {'00': 'Brak Kabla', '05': 'RG58', '06': 'RG174', '07': 'H155'}
MAPOWANIE_ZLACZY_T1 = {
    '000': 'Brak Złącza', '100': 'FAKRA Cod. E (F)', '101': 'FAKRA Cod. E (M)', '102': 'FME (F)', '103': 'FME (M)',
    '104': 'BNC (F)', '105': 'BNC (M)', '106': 'SMA (F)', '107': 'SMA (M)', '108': 'R-SMA (F)',
    '109': 'R-SMA (M)', '110': 'SMB (F)', '111': 'SMB (M)', '112': 'UHF (F)', '113': 'UHF (M)',
    '114': 'mini UHF (F)', '115': 'mini UHF (M)', '116': 'FAKRA Cod. A (F)', '117': 'FAKRA Cod. A (M)',
    '118': 'FAKRA Cod. B (F)', '119': 'FAKRA Cod. B (M)', '120': 'FAKRA Cod. C (F)', '121': 'FAKRA Cod. C (M)',
    '122': 'FAKRA Cod. D (F)', '123': 'FAKRA Cod. D (M)', '124': 'FAKRA Cod. M (F)', '125': 'FAKRA Cod. M (M)',
    '126': 'FAKRA Cod. N (F)', '127': 'FAKRA Cod. N (M)', '128': 'FAKRA Cod. Z (F)', '129': 'FAKRA Cod. Z (M)',
    '130': 'M10 (F)', '131': 'M10 (M)', '132': 'FAKRA Cod. F (F)', '133': 'FAKRA Cod. F (M)',
    '134': 'FAKRA Cod. G (F)', '135': 'FAKRA Cod. G (M)', '136': 'FAKRA Cod. H (F)', '137': 'FAKRA Cod. H (M)',
    '138': 'FAKRA Cod. I (F)', '139': 'FAKRA Cod. I (M)', '140': 'FAKRA Cod. K (F)', '141': 'FAKRA Cod. K (M)',
    '142': 'FAKRA Cod. L (F)', '143': 'FAKRA Cod. L (M)',
}
MAPOWANIE_ZLACZY_T2 = {
    '000': 'Brak Złącza', '500': 'FAKRA Cod. M (F)', '501': 'FAKRA Cod. M (M)', '502': 'FAKRA Cod. N (F)',
    '503': 'FAKRA Cod. N (M)', '504': 'FAKRA Cod. Z (F)', '505': 'FAKRA Cod. Z (M)', '506': 'M10 (F)',
    '507': 'M10 (M)', '508': 'FAKRA Cod. F (F)', '509': 'FAKRA Cod. F (M)', '510': 'FAKRA Cod. G (F)',
    '511': 'FAKRA Cod. G (M)', '512': 'FAKRA Cod. H (F)', '513': 'FAKRA Cod. H (M)', '514': 'FAKRA Cod. I (F)',
    '515': 'FAKRA Cod. I (M)', '516': 'FAKRA Cod. K (F)', '517': 'FAKRA Cod. K (M)', '518': 'FAKRA Cod. L (F)',
    '519': 'FAKRA Cod. L (M)', '520': 'mini UHF (F)', '521': 'mini UHF (M)', '522': 'FAKRA Cod. A (F)',
    '523': 'FAKRA Cod. A (M)', '524': 'FAKRA Cod. B (F)', '525': 'FAKRA Cod. B (M)', '526': 'FAKRA Cod. C (F)',
    '527': 'FAKRA Cod. C (M)', '528': 'FAKRA Cod. D (F)', '529': 'FAKRA Cod. D (M)', '530': 'FAKRA Cod. E (F)',
    '531': 'FAKRA Cod. E (M)', '532': 'FME (F)', '533': 'FME (M)', '534': 'BNC (F)', '535': 'BNC (M)',
    '536': 'SMA (F)', '537': 'SMA (M)', '538': 'R-SMA (F)', '539': 'R-SMA (M)', '540': 'SMB (F)',
    '541': 'SMB (M)', '542': 'UHF (F)', '543': 'UHF (M)',
}
MAPOWANIE_DLUGOSCI = {
    '030': '3.0 m', '035': '3.5 m', '040': '4.0 m', '045': '4.5 m',
    '050': '5.0 m', '055': '5.5 m', '060': '6.0 m', '065': '6.5 m',
    '070': '7.0 m', '075': '7.5 m', '080': '8.0 m', '085': '8.5 m',
    '090': '9.0 m', '095': '9.5 m', '100': '10.0 m', '105': '10.5 m',
    '110': '11.0 m'
}


def get_map_values(mapping):
    return list(mapping.values())


def get_key_by_value(mapping, value):
    for key, val in mapping.items():
        if val == value:
            return key
    return None


# ====================================================================
# II. DEFINICJE MOTYWÓW
# ====================================================================

THEME_CLEAN_LIGHT = {
    'ACCENT_COLOR': "#008080", 'HOVER_COLOR': "#005a5a", 'MAIN_BG': "gray90", 'CARD_BG': "white",
    'TEXT_COLOR': "gray20", 'DISABLED_TEXT_COLOR': "gray50", 'DROPDOWN_BG': "gray95", 'DROPDOWN_HOVER': "gray85",
    'CTK_MODE': "Light", 'CTK_THEME': "blue", 'NAME': "1. Czysty (Jasny)"
}

THEME_BLACK = {
    'ACCENT_COLOR': "#00FFFF", 'HOVER_COLOR': "#00E0E0",
    'MAIN_BG': "#101010", 'CARD_BG': "#000000",
    'TEXT_COLOR': "white", 'DISABLED_TEXT_COLOR': "gray60",
    # DROPDOWN_BG na ciemny szary dla widoczności listy
    'DROPDOWN_BG': "#303030",
    'DROPDOWN_HOVER': "#404040",
    'CTK_MODE': "Dark", 'CTK_THEME': "blue", 'NAME': "2. Czarny (Black Mode)"
}

THEME_EARTH_MASCULINE = {
    'ACCENT_COLOR': "#8B4513", 'HOVER_COLOR': "#A0522D", 'MAIN_BG': "#D2B48C", 'CARD_BG': "#F5DEB3",
    'TEXT_COLOR': "#5A4C3D", 'DISABLED_TEXT_COLOR': "gray50", 'DROPDOWN_BG': "#E0C8A8", 'DROPDOWN_HOVER': "#D5BF9F",
    'CTK_MODE': "Light", 'CTK_THEME': "green", 'NAME': "3. Ziemia (Męski)"
}

THEME_ROSE_FEMININE = {
    'ACCENT_COLOR': "#E57373", 'HOVER_COLOR': "#D32F2F", 'MAIN_BG': "#FFF0F5", 'CARD_BG': "white",
    'TEXT_COLOR': "#5C2037", 'DISABLED_TEXT_COLOR': "gray50", 'DROPDOWN_BG': "#FCE4EC", 'DROPDOWN_HOVER': "#F8BBD0",
    'CTK_MODE': "Light", 'CTK_THEME': "blue", 'NAME': "4. Różany (Żeński)"
}

ALL_THEMES = {
    "Czysty": THEME_CLEAN_LIGHT,
    "Czarny": THEME_BLACK,
    "Ziemia": THEME_EARTH_MASCULINE,
    "Różany": THEME_ROSE_FEMININE
}


# ====================================================================
# III. KLASA GENERATORA Z PŁYNNĄ ZMIANĄ MOTYWU
# ====================================================================

class GeneratorKabliApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.current_theme_key = "Czysty"
        self.current_theme_colors = ALL_THEMES[self.current_theme_key]
        self._load_theme_colors(self.current_theme_colors)

        self.GLOBAL_FONT = ctk.CTkFont(family="Arial", size=13)
        self.GLOBAL_FONT_BOLD = ctk.CTkFont(family="Arial", size=14, weight="bold")

        self.title(f"Generator Numerów Kabli - Motyw: {self.current_theme_key}")
        self.geometry("1000x700")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        ctk.set_appearance_mode(self.CTK_MODE)
        ctk.set_default_color_theme(self.CTK_THEME)

        self.mapy = {
            'T1': MAPOWANIE_ZLACZY_T1, 'T2': MAPOWANIE_ZLACZY_T2,
            'O': MAPOWANIE_ORIENTACJI_DO_WYBORU, 'K': MAPOWANIE_KABLA, 'D': MAPOWANIE_DLUGOSCI
        }

        self.kod_t1 = tk.StringVar(value=get_map_values(self.mapy['T1'])[0])
        self.kod_o1 = tk.StringVar(value=get_map_values(self.mapy['O'])[0])
        self.kod_t2 = tk.StringVar(value=get_map_values(self.mapy['T2'])[0])
        self.kod_o2 = tk.StringVar(value=get_map_values(self.mapy['O'])[0])
        self.kod_k = tk.StringVar(value=get_map_values(self.mapy['K'])[0])
        self.kod_d = tk.StringVar(value=get_map_values(self.mapy['D'])[0])
        self.theme_var = ctk.StringVar(value=self.current_theme_key)

        self.menu_refs = {}
        self.label_refs = {}
        self.frame_refs = {}
        self.button_refs = {}

        self.utworz_interfejs()
        self.bind_events()
        self.aktualizuj_stan_gui()
        self.generuj_numer_katalogowy()

    def _load_theme_colors(self, colors):
        """Ładuje kolory motywu do zmiennych instancji."""
        self.ACCENT_COLOR = colors['ACCENT_COLOR']
        self.HOVER_COLOR = colors['HOVER_COLOR']
        self.MAIN_BG = colors['MAIN_BG']
        self.CARD_BG = colors['CARD_BG']
        self.TEXT_COLOR = colors['TEXT_COLOR']
        self.DISABLED_TEXT_COLOR = colors['DISABLED_TEXT_COLOR']
        self.DROPDOWN_BG = colors['DROPDOWN_BG']
        self.DROPDOWN_HOVER = colors['DROPDOWN_HOVER']
        self.CTK_MODE = colors['CTK_MODE']
        self.CTK_THEME = colors['CTK_THEME']

    def set_theme(self, new_theme_key):
        """Dynamicznie zmienia motyw aplikacji bez niszczenia widgetów."""
        if new_theme_key not in ALL_THEMES:
            return

        self.current_theme_key = new_theme_key
        new_colors = ALL_THEMES[new_theme_key]
        self._load_theme_colors(new_colors)

        ctk.set_appearance_mode(self.CTK_MODE)
        self.config(bg=self.MAIN_BG)
        self.title(f"Generator Numerów Kabli - Motyw: {self.current_theme_key}")

        self._aktualizuj_wszystkie_kolory()

        self.aktualizuj_stan_gui()
        self.generuj_numer_katalogowy()

    def _aktualizuj_kolory_ramki(self, frame, is_card=True):
        """Pomocnicza funkcja do aktualizacji kolorów ramki."""
        if is_card:
            border_color = "gray80" if self.CTK_MODE == "Light" else "gray30"
            frame.configure(fg_color=self.CARD_BG, border_color=border_color)
        else:
            frame.configure(fg_color=self.MAIN_BG)

    def _aktualizuj_kolory_menu(self, menu):
        """Pomocnicza funkcja do aktualizacji kolorów CTkOptionMenu."""
        # W motywie czarnym musimy wymusić czarny tekst wewnątrz drop-down,
        # ponieważ DROPDOWN_BG jest ciemny.
        dropdown_text_color_val = "gray10" if self.current_theme_key == "Czarny" else self.TEXT_COLOR

        # W motywie czarnym wymuszamy czarny tekst na samym przycisku,
        # ponieważ jego tło jest jasne (wynikające z globalnej konfiguracji CTkOptionMenu)
        menu_text_color_val = "gray10" if self.current_theme_key == "Czarny" else self.TEXT_COLOR

        menu.configure(
            text_color=menu_text_color_val,  # KLUCZOWA ZMIANA: Tekst wyświetlany na przycisku menu
            dropdown_text_color=dropdown_text_color_val,  # Tekst na liście opcji
            dropdown_fg_color=self.DROPDOWN_BG,
            dropdown_hover_color=self.DROPDOWN_HOVER,
            fg_color="white" if self.current_theme_key == "Czarny" else self.DROPDOWN_BG,
            # Wymuszamy białe tło przycisku na Black Mode
            button_color=self.ACCENT_COLOR,
            button_hover_color=self.HOVER_COLOR
        )

    def _aktualizuj_wszystkie_kolory(self):
        """Iteruje przez wszystkie zarejestrowane widgety i aktualizuje ich kolory."""

        self._aktualizuj_kolory_ramki(self.main_frame, is_card=False)
        self._aktualizuj_kolory_ramki(self.theme_frame, is_card=True)
        self._aktualizuj_kolory_ramki(self.result_frame, is_card=True)

        for frame_ref in self.frame_refs.values():
            self._aktualizuj_kolory_ramki(frame_ref, is_card=True)

        for menu_ref in self.menu_refs.values():
            self._aktualizuj_kolory_menu(menu_ref)

        self.label_refs['theme_label'].configure(text_color=self.ACCENT_COLOR)
        self.label_refs['result_title'].configure(text_color=self.TEXT_COLOR)

        for label_ref in self.label_refs['section_labels']:
            label_ref.configure(text_color=self.ACCENT_COLOR)

        self.button_refs['zamawiam'].configure(
            fg_color=self.ACCENT_COLOR,
            hover_color=self.HOVER_COLOR
        )

    def utworz_interfejs(self):
        """Tworzy interfejs tylko RAZ."""

        self.main_frame = ctk.CTkFrame(self, corner_radius=10, fg_color=self.MAIN_BG)
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        self.main_frame.grid_columnconfigure((0, 2), weight=3)
        self.main_frame.grid_columnconfigure((1, 3), weight=1)

        # --- SEKCJA WYBORU MOTYWU ---
        border_color = "gray80" if self.CTK_MODE == "Light" else "gray30"

        self.theme_frame = ctk.CTkFrame(self.main_frame, fg_color=self.CARD_BG, corner_radius=10,
                                        border_color=border_color, border_width=1)
        self.theme_frame.grid(row=0, column=0, columnspan=4, sticky="ew", padx=10, pady=(0, 10))
        self.theme_frame.grid_columnconfigure(0, weight=1)
        self.frame_refs['theme_frame'] = self.theme_frame

        theme_label = ctk.CTkLabel(self.theme_frame, text="Zmień Motyw:", font=self.GLOBAL_FONT_BOLD,
                                   text_color=self.ACCENT_COLOR)
        theme_label.grid(row=0, column=0, sticky='w', padx=15, pady=10)
        self.label_refs['theme_label'] = theme_label

        # Ustawienie kolorów dla menu motywów
        dropdown_text_color_val = "gray10" if self.current_theme_key == "Czarny" else self.TEXT_COLOR
        menu_text_color_val = "gray10" if self.current_theme_key == "Czarny" else self.TEXT_COLOR
        menu_fg_color_val = "white" if self.current_theme_key == "Czarny" else self.DROPDOWN_BG

        theme_options = list(ALL_THEMES.keys())
        theme_menu = ctk.CTkOptionMenu(
            self.theme_frame,
            values=theme_options,
            command=self.set_theme,
            variable=self.theme_var,
            font=self.GLOBAL_FONT,
            width=200,

            fg_color=menu_fg_color_val, button_color=self.ACCENT_COLOR, button_hover_color=self.HOVER_COLOR,
            dropdown_fg_color=self.DROPDOWN_BG, dropdown_hover_color=self.DROPDOWN_HOVER,
            text_color=menu_text_color_val,
            dropdown_text_color=dropdown_text_color_val
        )
        theme_menu.grid(row=0, column=1, sticky='e', padx=15, pady=10)
        self.menu_refs['theme_menu'] = theme_menu

        # --- SEKCJE WYBORU KABLA ---
        start_row = 1
        self.label_refs['section_labels'] = []

        self.menu_t1_ref, card_frame_t1 = self.tworz_sekcje_wyboru(self.main_frame, "1. Złącze T1 (3c) 🔌",
                                                                   self.mapy['T1'], self.kod_t1, start_row + 0, 0,
                                                                   wide=True)
        self.menu_t2_ref, card_frame_t2 = self.tworz_sekcje_wyboru(self.main_frame, "2. Złącze T2 (3c) 🔌",
                                                                   self.mapy['T2'], self.kod_t2, start_row + 0, 2,
                                                                   wide=True)
        self.menu_o1_ref, card_frame_o1 = self.tworz_sekcje_wyboru(self.main_frame, "3. Orientacja O1 (2c) 📐",
                                                                   self.mapy['O'], self.kod_o1, start_row + 2, 0,
                                                                   wide=False)
        self.menu_o2_ref, card_frame_o2 = self.tworz_sekcje_wyboru(self.main_frame, "4. Orientacja O2 (2c) 📐",
                                                                   self.mapy['O'], self.kod_o2, start_row + 2, 2,
                                                                   wide=False)
        self.menu_k_ref, card_frame_k = self.tworz_sekcje_wyboru(self.main_frame, "5. Typ Kabla K (2c) 🧵",
                                                                 self.mapy['K'], self.kod_k, start_row + 4, 0,
                                                                 wide=False)
        self.menu_d_ref, card_frame_d = self.tworz_sekcje_wyboru(self.main_frame, "6. Długość Kabla D (3c) 📏",
                                                                 self.mapy['D'], self.kod_d, start_row + 4, 2,
                                                                 wide=False)

        self.frame_refs['T1'] = card_frame_t1
        self.frame_refs['T2'] = card_frame_t2
        self.frame_refs['O1'] = card_frame_o1
        self.frame_refs['O2'] = card_frame_o2
        self.frame_refs['K'] = card_frame_k
        self.frame_refs['D'] = card_frame_d

        ctk.CTkLabel(self.main_frame, text="", height=20, fg_color=self.MAIN_BG).grid(row=start_row + 6, columnspan=4,
                                                                                      sticky="ew")

        # --- SEKCJA WYNIKU I PRZYCISK ---
        self.result_frame = ctk.CTkFrame(self.main_frame, fg_color=self.CARD_BG, corner_radius=10,
                                         border_color=border_color, border_width=1)
        self.result_frame.grid(row=start_row + 7, column=0, columnspan=4, sticky="ew", padx=10, pady=10)
        self.result_frame.grid_columnconfigure(0, weight=4)
        self.result_frame.grid_columnconfigure(1, weight=1)
        self.frame_refs['result_frame'] = self.result_frame

        result_title_label = ctk.CTkLabel(self.result_frame, text="NUMER KATALOGOWY:", font=self.GLOBAL_FONT_BOLD,
                                          text_color=self.TEXT_COLOR)
        result_title_label.grid(row=0, column=0, sticky='w', padx=15, pady=(10, 0))
        self.label_refs['result_title'] = result_title_label

        self.wynik_label = ctk.CTkLabel(self.result_frame, text="---", font=ctk.CTkFont(size=26, weight="bold"),
                                        text_color=self.ACCENT_COLOR)
        self.wynik_label.grid(row=1, column=0, sticky='w', padx=15, pady=(0, 10))

        zamawiam_button = ctk.CTkButton(self.result_frame, text="ZAMAWIAM",
                                        command=lambda: self.generuj_numer_katalogowy(pokaz_alert=True),
                                        font=ctk.CTkFont(size=14, weight="bold"),
                                        height=50,
                                        fg_color=self.ACCENT_COLOR,
                                        hover_color=self.HOVER_COLOR
                                        )
        zamawiam_button.grid(row=0, column=1, rowspan=2, sticky='e', padx=15, pady=10)
        self.button_refs['zamawiam'] = zamawiam_button

        for i in [1, 3, 5]:
            self.main_frame.grid_rowconfigure(i, weight=1)

    def tworz_sekcje_wyboru(self, frame, label_text, mapa_danych, ctk_variable, start_row, start_column, wide=False):
        border_color = "gray80" if self.CTK_MODE == "Light" else "gray30"

        card_frame = ctk.CTkFrame(frame, fg_color=self.CARD_BG, corner_radius=10, border_color=border_color,
                                  border_width=1)
        span = 2 if wide else 1
        card_frame.grid(row=start_row, column=start_column, columnspan=span,
                        rowspan=2, sticky="nsew", padx=10, pady=10)
        card_frame.grid_columnconfigure(0, weight=1)

        section_label = ctk.CTkLabel(card_frame, text=label_text,
                                     font=self.GLOBAL_FONT_BOLD, text_color=self.ACCENT_COLOR
                                     )
        section_label.grid(row=0, column=0, sticky='w', padx=15, pady=(15, 5))
        self.label_refs['section_labels'].append(section_label)

        menu_width = 300 if wide else 180

        # Konfiguracja kolorów dla menu na podstawie motywu
        dropdown_text_color_val = "gray10" if self.current_theme_key == "Czarny" else self.TEXT_COLOR
        menu_text_color_val = "gray10" if self.current_theme_key == "Czarny" else self.TEXT_COLOR
        menu_fg_color_val = "white" if self.current_theme_key == "Czarny" else self.DROPDOWN_BG

        option_menu = ctk.CTkOptionMenu(
            card_frame,
            values=get_map_values(mapa_danych),
            command=self.on_selection_change,
            variable=ctk_variable,
            font=self.GLOBAL_FONT,
            text_color=menu_text_color_val,  # KLUCZOWA ZMIANA: Tekst wyświetlany na przycisku menu

            dropdown_font=self.GLOBAL_FONT,
            dropdown_text_color=dropdown_text_color_val,  # Tekst w rozwijanej liście
            dropdown_fg_color=self.DROPDOWN_BG,
            dropdown_hover_color=self.DROPDOWN_HOVER,

            fg_color=menu_fg_color_val,  # Tło przycisku menu
            button_color=self.ACCENT_COLOR,
            button_hover_color=self.HOVER_COLOR,

            width=menu_width,
            height=35

        )
        option_menu.grid(row=1, column=0, sticky='ew', padx=15, pady=(0, 15))

        return option_menu, card_frame

    def bind_events(self):
        self.kod_t1.trace_add("write", lambda *args: self.on_selection_change(self.kod_t1.get()))
        self.kod_o1.trace_add("write", lambda *args: self.on_selection_change(self.kod_o1.get()))
        self.kod_t2.trace_add("write", lambda *args: self.on_selection_change(self.kod_t2.get()))
        self.kod_o2.trace_add("write", lambda *args: self.on_selection_change(self.kod_o2.get()))
        self.kod_k.trace_add("write", lambda *args: self.on_selection_change(self.kod_k.get()))
        self.kod_d.trace_add("write", lambda *args: self.on_selection_change(self.kod_d.get()))

    def on_selection_change(self, value):
        self.aktualizuj_stan_gui()
        self.generuj_numer_katalogowy()

    def aktualizuj_stan_gui(self):
        t1_val = get_key_by_value(self.mapy['T1'], self.kod_t1.get())
        t2_val = get_key_by_value(self.mapy['T2'], self.kod_t2.get())
        k_val = get_key_by_value(self.mapy['K'], self.kod_k.get())

        self._toggle_menu_state(self.menu_o1_ref, 'O1', t1_val != '000', self.kod_o1, self.mapy['O'])
        self._toggle_menu_state(self.menu_o2_ref, 'O2', t2_val != '000', self.kod_o2, self.mapy['O'])
        self._toggle_menu_state(self.menu_d_ref, 'D', k_val != '00', self.kod_d, self.mapy['D'])

    def _toggle_menu_state(self, menu, name, should_enable, variable, default_map):
        if should_enable:
            menu.configure(state="normal", text_color=self.TEXT_COLOR)

            # Wymuszamy czarny tekst, gdy menu jest aktywne w Czarnym motywie
            if self.current_theme_key == "Czarny":
                menu.configure(text_color="gray10")
            else:
                menu.configure(text_color=self.TEXT_COLOR)

            menu.configure(values=get_map_values(default_map))
            if variable.get() == f"--- POMINIĘTE {name} ---":
                new_value = get_map_values(default_map)[0]
                variable.set(new_value)
                menu.set(new_value)
        else:
            menu.configure(state="disabled", text_color=self.DISABLED_TEXT_COLOR)
            disabled_value = f"--- POMINIĘTE {name} ---"
            variable.set(disabled_value)
            menu.configure(values=[disabled_value])
            menu.set(disabled_value)

    def generuj_numer_katalogowy(self, pokaz_alert=False):
        T1 = get_key_by_value(self.mapy['T1'], self.kod_t1.get())
        O1 = get_key_by_value(self.mapy['O'], self.kod_o1.get())
        T2 = get_key_by_value(self.mapy['T2'], self.kod_t2.get())
        O2 = get_key_by_value(self.mapy['O'], self.kod_o2.get())
        K = get_key_by_value(self.mapy['K'], self.kod_k.get())
        D = get_key_by_value(self.mapy['D'], self.kod_d.get())

        segmenty = []
        wszystko_ok = True

        if T1 is not None:
            segmenty.append(T1)
            if T1 != '000' and 'POMINIĘTE' not in self.kod_o1.get():
                segmenty.append(O1)
            elif T1 != '000' and 'POMINIĘTE' in self.kod_o1.get():
                wszystko_ok = False

        if T2 is not None:
            segmenty.append(T2)
            if T2 != '000' and 'POMINIĘTE' not in self.kod_o2.get():
                segmenty.append(O2)
            elif T2 != '000' and 'POMINIĘTE' in self.kod_o2.get():
                wszystko_ok = False

        if K is not None:
            segmenty.append(K)
            if K != '00' and 'POMINIĘTE' not in self.kod_d.get():
                segmenty.append(D)
            elif K != '00' and 'POMINIĘTE' in self.kod_d.get():
                wszystko_ok = False

        numer_katalogowy = "".join(segmenty)
        dlugosc_numeru = len(numer_katalogowy)

        if numer_katalogowy and wszystko_ok:
            self.wynik_label.configure(text=f"{numer_katalogowy} ({dlugosc_numeru} cyfr)", text_color=self.ACCENT_COLOR)
        else:
            self.wynik_label.configure(text="--- BRAK DANYCH (BŁĄD) ---", text_color="#e74c3c")

        if pokaz_alert and wszystko_ok and numer_katalogowy:
            messagebox.showinfo("Potwierdzenie Zamówienia",
                                f"Złożono zamówienie na produkt:\n{numer_katalogowy}\nDługość kodu: {dlugosc_numeru} cyfr")
        elif pokaz_alert and not wszystko_ok:
            messagebox.showerror("Błąd Weryfikacji",
                                 "Nie wybrano wymaganych orientacji/długości. Proszę sprawdzić wszystkie aktywne pola.")


# ====================================================================
# IV. URUCHOMIENIE APLIKACJI
# ====================================================================

if __name__ == "__main__":
    app = GeneratorKabliApp()
    app.mainloop()