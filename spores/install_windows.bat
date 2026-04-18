@echo off
echo 🦠 AMOEBA SPORE — windows
powershell -Command "Invoke-WebRequest -Uri 'https://ollama.com/download/OllamaSetup.exe' -OutFile '%TEMP%\OllamaSetup.exe'"
start /wait %TEMP%\OllamaSetup.exe /S
timeout /t 5
ollama pull llama3.2:1b
echo Done. Return to AMOEBA and press CONNECT OLLAMA.
pause
