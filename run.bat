@echo off
setlocal
cd /d "%~dp0"

set PY=.venv\Scripts\python.exe
if not exist "%PY%" set PY=python

rem Install deps on first run if missing
"%PY%" -c "import folium,branca" 2>nul || "%PY%" -m pip install -r requirements.txt

rem Build the map and open it in the default browser. No server: nothing to shut down.
"%PY%" src\main.py
