@echo off
echo Only use this script if you don't have Python or the other prerequisites installed.
pause
winget install -e --id Python.Python.3.12
pause
start cmd.exe /c pip install blinkpy
start cmd.exe /c pip install asyncio
