@echo off
setlocal
cd /d "%~dp0"
if errorlevel 1 goto ubicacion
set "PYTHONHOME="
set "PYTHONPATH="
set "PYTHONUTF8=1"
echo Instalacion SBD para Windows 11. Hace falta Internet la primera vez.
echo Extrae el ZIP en una carpeta local antes de continuar.
echo.
if exist ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" "soporte\preparar.py"
    goto fin
)
for %%V in (3.14 3.13 3.12 3.11 3.10) do (
    py -%%V -c "import sys; sys.exit(0 if sys.implementation.name == 'cpython' and sys.version_info[0] == 3 and sys.version_info[1] in range(10,15) else 1)" >nul 2>&1
    if not errorlevel 1 (
        py -%%V "soporte\preparar.py"
        goto fin
    )
)
python -c "import sys; sys.exit(0 if sys.implementation.name == 'cpython' and sys.version_info[0] == 3 and sys.version_info[1] in range(10,15) else 1)" >nul 2>&1
if not errorlevel 1 (
    python "soporte\preparar.py"
    goto fin
)
echo No se encontro CPython 3.10 a 3.14.
echo Instala Python 3.14 para tu usuario desde https://www.python.org/downloads/windows/
echo Incluye el lanzador py. Si solo tienes Python 3.15, puedes conservarlo e instalar 3.14 tambien.
echo Despues cierra esta ventana y vuelve a ejecutar este instalador.
pause
exit /b 1
:ubicacion
echo No se puede acceder a la carpeta. Extrae el ZIP en una carpeta local con permiso de escritura.
pause
exit /b 1
:fin
set "SBD_RESULT=%ERRORLEVEL%"
echo.
if not "%SBD_RESULT%"=="0" echo No se completo la preparacion. Revisa el mensaje anterior y la guia.
pause
exit /b %SBD_RESULT%
