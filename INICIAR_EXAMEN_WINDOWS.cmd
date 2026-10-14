@echo off
setlocal
cd /d "%~dp0"
if errorlevel 1 exit /b 1
set "PYTHONHOME="
set "PYTHONPATH="
set "PYTHONUTF8=1"
if not exist ".venv\Scripts\python.exe" (
    echo Primero ejecuta INSTALAR_WINDOWS.cmd con conexion a Internet.
    pause
    exit /b 1
)
".venv\Scripts\python.exe" "soporte\iniciar.py"
set "SBD_RESULT=%ERRORLEVEL%"
if not "%SBD_RESULT%"=="0" pause
exit /b %SBD_RESULT%
