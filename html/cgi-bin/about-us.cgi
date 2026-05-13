#!/usr/bin/env python3
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import html
import sys

sys.stdout.reconfigure(encoding="utf-8")

form = cgi.FieldStorage()

print("Content-Type: text/html; charset=utf-8")
print()

print(f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> About us page</title>
    <link rel="stylesheet" href="../css/style.css" type="text/css">
</head>
<body>
    <div class="header-row">
        <h1> About us</h1>
    </div>
<main>
kinda still empty but info about us is gonna be here soon
</main>
    <footer>
        <p>
            <a href="https://github.com/JuJu-Inf/Semester-Projekt-OS-Webcomputing" target="_blank" rel="noopener noreferrer">
                <img src="../images/GitHub_Logo.png" alt="GitHub logo" class="logo">
            </a>

            <a href="https://www.th-brandenburg.de/" target="_blank" rel="noopener noreferrer" class="logo-link">
                <img src="../images/THB_logo.png" alt="TH Brandenburg logo" class="logo">
            </a>

            <a href="http://pan.th-brandenburg.de/~radkep/cgi-bin/about-us.cgi" class="logo-link">
                <img src="../images/THB_logo.png" alt="About us logo" class="about-logo">
            </a>
        </p>
    </footer>
</body>
</html>""")
