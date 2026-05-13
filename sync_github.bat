@echo off
cd /d "c:\Users\gilma\Desktop\portfolio.github.io-main\portfolio.github.io-main"

echo Pull des changements distants...
"C:\Program Files\Git\bin\git.exe" pull origin main --allow-unrelated-histories

echo.
echo Push vers GitHub...
"C:\Program Files\Git\bin\git.exe" push -u origin main

echo.
echo Synchronisation complete!
pause
