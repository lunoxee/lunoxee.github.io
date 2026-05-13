#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# ============================================
# MODERNISER INDEX.HTML
# ============================================
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Ajouter animations CSS et modernisations
animations_css = '''
        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes floatAnimation {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-8px); }
        }

        @keyframes slideInLeft {
            from {
                opacity: 0;
                transform: translateX(-30px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }

        @keyframes slideInRight {
            from {
                opacity: 0;
                transform: translateX(30px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }

        @keyframes glassGlow {
            0%, 100% {
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1), inset 0 0 20px rgba(255, 255, 255, 0.05);
            }
            50% {
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2), inset 0 0 30px rgba(255, 255, 255, 0.1);
            }
        }
'''

# Remplacer la section moon-top
index_content = re.sub(
    r'        /\* LUNE EN HAUT A DROITE \*/(.*?)opacity: 0\.8;(.*?)\}',
    r'''        /* LUNE EN HAUT A DROITE */
        .moon-top {
            position: absolute;
            top: 20px;
            right: 20px;
            width: 120px;
            height: 120px;
            background: url("Lune 1.png") no-repeat center;
            background-size: contain;
            opacity: 0.85;
            animation: floatAnimation 4s ease-in-out infinite;
            filter: drop-shadow(0 4px 12px rgba(255, 255, 255, 0.1));
        }''',
    index_content,
    flags=re.DOTALL
)

# Remplacer la section moon-bottom
index_content = re.sub(
    r'        /\* LUNE EN BAS A GAUCHE \*/(.*?)z-index: -1;(.*?)\}',
    r'''        /* LUNE EN BAS A GAUCHE */
        .moon-bottom {
            position: fixed;
            bottom: 20px;
            left: 20px;
            width: 100px;
            height: 100px;
            background: url("Lune 2.png") no-repeat center;
            background-size: contain;
            opacity: 0.6;
            z-index: -1;
            animation: floatAnimation 5s ease-in-out infinite reverse;
            filter: drop-shadow(0 4px 12px rgba(255, 255, 255, 0.05));
        }''',
    index_content,
    flags=re.DOTALL
)

# Ajouter les animations après les variables CSS
index_content = index_content.replace(
    '        }\n\n        body {',
    animations_css + '\n        }\n\n        body {'
)

# Améliorer le style du header avec animation et espacement
index_content = re.sub(
    r'        header \{(.*?)padding: 120px 20px 60px;(.*?)\}',
    r'''        header {
            text-align: center;
            padding: 140px 20px 80px;
            animation: fadeInDown 0.8s ease-out;
        }''',
    index_content,
    flags=re.DOTALL
)

# Ajouter glassmorphism au about-box
index_content = re.sub(
    r'        \.about-box \{(.*?)box-shadow: 0 15px 35px rgba\(0,0,0,0\.2\);(.*?)\}',
    r'''        .about-box {
            background-color: rgba(85, 85, 85, 0.7);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: var(--border-round);
            padding: 40px 60px;
            margin-bottom: 50px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
            text-align: center;
            animation: slideInRight 0.8s ease-out;
            transition: all 0.3s ease;
        }

        .about-box:hover {
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            box-shadow: 0 12px 40px rgba(0, 0, 0, 0.25);
        }''',
    index_content,
    flags=re.DOTALL
)

# Améliorer les cartes de projets avec glassmorphism
index_content = re.sub(
    r'        \.project-card \{(.*?)box-shadow: 0 10px 25px rgba\(0,0,0,0\.1\);(.*?)\}',
    r'''        .project-card {
            background: rgba(85, 85, 85, 0.6);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 30px;
            text-align: center;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
            animation: slideInLeft 0.8s ease-out;
        }

        .project-card:hover {
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            transform: translateY(-5px);
            box-shadow: 0 12px 40px rgba(0, 0, 0, 0.2);
        }''',
    index_content,
    flags=re.DOTALL
)

# Améliorer les navigations avec bordures fines
index_content = re.sub(
    r'        nav a \{(.*?)border-bottom: 1px solid transparent;(.*?)\}',
    r'''        nav a {
            color: var(--text-sub);
            text-decoration: none;
            font-size: 1.1rem;
            transition: all 0.3s ease;
            border-bottom: 1px solid transparent;
            padding-bottom: 2px;
        }''',
    index_content,
    flags=re.DOTALL
)

# Sauvegarder index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_content)
print('✓ index.html modernisé avec animations et glassmorphism')

# ============================================
# MODERNISER CV.HTML
# ============================================
with open('cv.html', 'r', encoding='utf-8') as f:
    cv_content = f.read()

# Ajouter animations et améliorations
cv_modernizations = '''
        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes slideInLeft {
            from {
                opacity: 0;
                transform: translateX(-30px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }

        @keyframes slideInRight {
            from {
                opacity: 0;
                transform: translateX(30px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }
'''

# Ajouter les animations
cv_content = cv_content.replace(
    '        }\n\n        body {',
    cv_modernizations + '\n        }\n\n        body {'
)

# Améliorer le container avec glassmorphism
cv_content = re.sub(
    r'        \.container \{(.*?)box-shadow: 0 20px 40px rgba\(0,0,0,0\.3\);(.*?)\}',
    r'''        .container {
            max-width: 900px;
            margin: 40px auto;
            padding: 40px;
            background: rgba(85, 85, 85, 0.7);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 40px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
            animation: fadeInDown 0.8s ease-out;
        }''',
    cv_content,
    flags=re.DOTALL
)

# Améliorer le header avec animation
cv_content = re.sub(
    r'        header \{(.*?)margin-bottom: 30px;(.*?)\}',
    r'''        header {
            display: flex;
            align-items: center;
            gap: 30px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            padding-bottom: 30px;
            margin-bottom: 30px;
            animation: slideInLeft 0.8s ease-out;
        }''',
    cv_content,
    flags=re.DOTALL
)

# Ajouter lunes au CV (en bas à droite et haut à gauche inversées)
cv_moon_styles = '''
        /* LUNE EN HAUT A GAUCHE */
        .moon-top {
            position: fixed;
            top: 20px;
            left: 20px;
            width: 100px;
            height: 100px;
            background: url("Lune 1.png") no-repeat center;
            background-size: contain;
            opacity: 0.6;
            filter: drop-shadow(0 4px 12px rgba(255, 255, 255, 0.05));
        }

        /* LUNE EN BAS A DROITE */
        .moon-bottom {
            position: fixed;
            bottom: 20px;
            right: 20px;
            width: 90px;
            height: 90px;
            background: url("Lune 2.png") no-repeat center;
            background-size: contain;
            opacity: 0.5;
            z-index: -1;
            filter: drop-shadow(0 4px 12px rgba(255, 255, 255, 0.05));
        }
'''

# Insérer les styles des lunes avant la balise body fermante
cv_content = cv_content.replace(
    '    </style>\n</head>',
    cv_moon_styles + '    </style>\n</head>'
)

# Ajouter les lunes dans le body
cv_content = cv_content.replace(
    '<body>\n\n    <div class="back-nav">',
    '<body>\n    <div class="moon-top"></div>\n    <div class="moon-bottom"></div>\n    <div class="back-nav">'
)

with open('cv.html', 'w', encoding='utf-8') as f:
    f.write(cv_content)
print('✓ cv.html modernisé avec lunes et glassmorphism')

# ============================================
# MODERNISER LUNOXE.HTML
# ============================================
with open('lunoxe.html', 'r', encoding='utf-8') as f:
    lunoxe_content = f.read()

# Ajouter animations
lunoxe_content = lunoxe_content.replace(
    '        }\n\n        body {',
    cv_modernizations + '\n        }\n\n        body {'
)

# Améliorer les sections doc avec glassmorphism
lunoxe_content = re.sub(
    r'        \.doc-section \{(.*?)box-shadow: 0 10px 25px rgba\(0,0,0,0\.1\);(.*?)\}',
    r'''        .doc-section {
            background: rgba(85, 85, 85, 0.7);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 40px;
            border-radius: 40px;
            margin-bottom: 30px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            animation: slideInLeft 0.8s ease-out;
            transition: all 0.3s ease;
        }

        .doc-section:hover {
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            box-shadow: 0 12px 40px rgba(0, 0, 0, 0.15);
        }''',
    lunoxe_content,
    flags=re.DOTALL
)

# Ajouter lunes à lunoxe.html
lunoxe_moon_styles = '''
        /* LUNE EN HAUT A DROITE */
        .moon-top {
            position: fixed;
            top: 20px;
            right: 20px;
            width: 100px;
            height: 100px;
            background: url("Lune 1.png") no-repeat center;
            background-size: contain;
            opacity: 0.6;
            filter: drop-shadow(0 4px 12px rgba(255, 255, 255, 0.05));
        }

        /* LUNE EN BAS A GAUCHE */
        .moon-bottom {
            position: fixed;
            bottom: 20px;
            left: 20px;
            width: 90px;
            height: 90px;
            background: url("Lune 2.png") no-repeat center;
            background-size: contain;
            opacity: 0.5;
            z-index: -1;
            filter: drop-shadow(0 4px 12px rgba(255, 255, 255, 0.05));
        }
'''

lunoxe_content = lunoxe_content.replace(
    '    </style>\n</head>',
    lunoxe_moon_styles + '    </style>\n</head>'
)

lunoxe_content = lunoxe_content.replace(
    '<body>\n\n    <div class="container">',
    '<body>\n    <div class="moon-top"></div>\n    <div class="moon-bottom"></div>\n    <div class="container">'
)

with open('lunoxe.html', 'w', encoding='utf-8') as f:
    f.write(lunoxe_content)
print('✓ lunoxe.html modernisé avec lunes et glassmorphism')

print('\n✨ Tous les fichiers HTML ont été modernisés avec succès!')
print('  - Lunes PNG intégrées')
print('  - Animations légères ajoutées')
print('  - Glassmorphism appliqué')
print('  - Espacements améliorés')
print('  - Bordures fines utilisées')
