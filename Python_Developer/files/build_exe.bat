@echo off
:: ============================================================
::  Universal Python to EXE Builder + Inno Setup Installer
::  Wybierz dowolny plik .py i konwertuj na .exe
::  Wystarczy double-click. Wymagany Python 3.8+ w PATH.
:: ============================================================
setlocal enabledelayedexpansion
title Python to EXE Builder + Inno Setup Installer

echo.
echo  =====================================================
echo   Universal Python EXE Builder
echo  =====================================================
echo.

:: --- Sprawdz Python ---
python --version >nul 2>&1
if errorlevel 1 (
    echo [BLAD] Python nie znaleziony w PATH.
    echo Pobierz Python z https://www.python.org/downloads/
    echo Przy instalacji zaznacz "Add Python to PATH"!
    pause
    exit /b 1
)
python --version
echo.

:: --- Wybor pliku Python ---
echo [1/6] Wybierz plik .py do konwersji:
echo.

:: Jesli plik podany jako argument
if not "%~1"=="" (
    set PYTHON_FILE=%~1
    echo Plik: !PYTHON_FILE!
) else (
    :: Dialog wyboru pliku (Windows Explorer)
    for /f "delims=" %%A in ('powershell -NoProfile -ExecutionPolicy Bypass -Command ^
        "(New-Object System.Windows.Forms.OpenFileDialog; ^
        $ofd = New-Object System.Windows.Forms.OpenFileDialog; ^
        $ofd.Filter = 'Python files (*.py)|*.py|All files (*.*)|*.*'; ^
        $ofd.InitialDirectory = '%cd%'; ^
        if ($ofd.ShowDialog() -eq 'OK') { $ofd.FileName } else { 'CANCEL' })"') do (
        set PYTHON_FILE=%%A
    )
    
    if "!PYTHON_FILE!"=="CANCEL" (
        echo [INFO] Anulowano wybor pliku.
        pause
        exit /b 0
    )
)

if not exist "!PYTHON_FILE!" (
    echo [BLAD] Plik nie znaleziony: !PYTHON_FILE!
    pause
    exit /b 1
)

:: Pobierz nazwę bez rozszerzenia
for /f "tokens=*" %%A in ("!PYTHON_FILE!") do (
    set FILENAME=%%~nA
    set FILENAME_NOEXT=%%~nA
)
set FILENAME_NOEXT=!FILENAME_NOEXT:.py=!

echo [OK] Plik: !PYTHON_FILE!
echo [OK] Nazwa EXE: !FILENAME_NOEXT!.exe
echo.

:: --- Srodowisko wirtualne ---
echo [2/6] Tworze srodowisko wirtualne...
if not exist ".venv" (
    python -m venv .venv
)
call .venv\Scripts\activate.bat

:: --- Instalacja PyInstaller ---
echo [3/6] Instaluje PyInstaller...
pip install --quiet --upgrade pyinstaller

:: --- Analiza zaleznisci (opcjonalnie) ---
echo [4/6] Analizuje zaleznosci Pythona...
if exist "requirements.txt" (
    echo Znaleziono requirements.txt - instaluje zaleznosci...
    pip install --quiet -r requirements.txt
)

:: --- Budowanie EXE ---
echo [5/6] Buduje !FILENAME_NOEXT!.exe (moze potrwac 1-2 minuty)...
pyinstaller ^
    --onefile ^
    --windowed ^
    --name !FILENAME_NOEXT! ^
    --hidden-import tkinter ^
    --hidden-import tkinter.ttk ^
    --hidden-import tkinter.filedialog ^
    --hidden-import tkinter.messagebox ^
    --hidden-import tkinter.scrolledtext ^
    "!PYTHON_FILE!"

if errorlevel 1 (
    echo.
    echo [BLAD] Budowanie nie powiodlo sie. Sprawdz powyzszy log.
    pause
    exit /b 1
)

echo.
echo  [OK] dist\!FILENAME_NOEXT!.exe - Sukces.
echo.

:: --- Inno Setup Installer (opcjonalnie) ---
set /p BUILD_INSTALLER="Czy chcesz budowac instalator? [T/N]: "
if /i "!BUILD_INSTALLER!"=="T" (
    echo [6/6] Tworzenie instalatora...
    
    if not exist "installer.iss" (
        echo.
        echo [INFO] Plik installer.iss nie znaleziony.
        echo Szukam Inno Setup...
    ) else (
        set ISCC=""
        if exist "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" set ISCC="C:\Program Files (x86)\Inno Setup 6\ISCC.exe"
        if exist "C:\Program Files\Inno Setup 6\ISCC.exe" set ISCC="C:\Program Files\Inno Setup 6\ISCC.exe"
        
        if %ISCC%=="" (
            echo  Inno Setup nie jest zainstalowany.
            echo  Pobieranie Inno Setup...
            powershell -NoProfile -ExecutionPolicy Bypass -Command ^
                "Invoke-WebRequest -Uri 'https://jrsoftware.org/download.php/is.exe' -OutFile 'inno_setup_installer.exe'"
            echo  Instalowanie Inno Setup cicho...
            inno_setup_installer.exe /VERYSILENT /SUPPRESSMSGBOXES /NORESTART
            del inno_setup_installer.exe
            if exist "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" set ISCC="C:\Program Files (x86)\Inno Setup 6\ISCC.exe"
            if exist "C:\Program Files\Inno Setup 6\ISCC.exe" set ISCC="C:\Program Files\Inno Setup 6\ISCC.exe"
        )
        
        if not %ISCC%=="" (
            echo Buduje instalator...
            %ISCC% installer.iss
            if errorlevel 1 (
                echo  [OSTRZEZENIE] Budowanie instalatora nie powiodlo sie.
                echo  Sam EXE jest dostepny w dist\!FILENAME_NOEXT!.exe
            ) else (
                echo.
                echo  =====================================================
                echo   GOTOWE!
                echo   - Sam program:  dist\!FILENAME_NOEXT!.exe
                echo   - INSTALATOR:   dist_installer\!FILENAME_NOEXT!_Setup.exe
                echo  =====================================================
                explorer dist_installer
                goto end
            )
        ) else (
            echo  [OSTRZEZENIE] Nie udalo sie zainstalowac Inno Setup.
            echo  Sam EXE jest dostepny w dist\!FILENAME_NOEXT!.exe
        )
    )
)

echo.
echo  =====================================================
echo   GOTOWE!  dist\!FILENAME_NOEXT!.exe
echo  =====================================================
explorer dist

:end
echo.
echo  WSKAZOWKA: 
echo  - Aby calkowicie usunac ostrzezenie SmartScreen,
echo    podpisz EXE certyfikatem Code Signing (np. Certum OV).
echo  - Mozesz tez uruchomic skrypt z argumentem:
echo    build_exe.bat "sciezka\do\pliku.py"
echo.
pause
