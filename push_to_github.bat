@echo off
cd /d "c:\Users\gilma\Desktop\portfolio.github.io-main\portfolio.github.io-main"

echo Verification de Git...
"C:\Program Files\Git\bin\git.exe" --version

echo.
echo Configuration de Git...
"C:\Program Files\Git\bin\git.exe" config --global user.name "Mathis Gil"
"C:\Program Files\Git\bin\git.exe" config --global user.email "gilmathis498@gmail.com"

echo.
echo Initialisation du depot Git...
"C:\Program Files\Git\bin\git.exe" init

echo.
echo Ajout de tous les fichiers...
"C:\Program Files\Git\bin\git.exe" add .

echo.
echo Creation du commit initial...
"C:\Program Files\Git\bin\git.exe" commit -m "Modernisation du portfolio: ajout des lunes PNG, animations et glassmorphism"

echo.
echo Configuration de la branche principale...
"C:\Program Files\Git\bin\git.exe" branch -M main

echo.
echo Ajout de la telecommande (remote) GitHub...
"C:\Program Files\Git\bin\git.exe" remote add origin https://github.com/lunoxee/portfolio.github.io.git

echo.
echo Push vers GitHub...
"C:\Program Files\Git\bin\git.exe" push -u origin main

echo.
echo Fait! Les fichiers ont ete envoyes sur GitHub.
pause
