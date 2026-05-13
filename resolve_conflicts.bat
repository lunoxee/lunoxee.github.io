@echo off
cd /d "c:\Users\gilma\Desktop\portfolio.github.io-main\portfolio.github.io-main"

echo Resoudre les conflits en gardant les versions locales...
"C:\Program Files\Git\bin\git.exe" checkout --ours cv.html index.html lunoxe.html

echo.
echo Ajouter les fichiers resolus...
"C:\Program Files\Git\bin\git.exe" add cv.html index.html lunoxe.html

echo.
echo Ajouter tous les autres fichiers...
"C:\Program Files\Git\bin\git.exe" add .

echo.
echo Creer le commit de fusion...
"C:\Program Files\Git\bin\git.exe" commit -m "Merge: Modernisation du portfolio avec lunes PNG, animations et glassmorphism"

echo.
echo Push vers GitHub...
"C:\Program Files\Git\bin\git.exe" push -u origin main

echo.
echo Synchronisation complete!
pause
