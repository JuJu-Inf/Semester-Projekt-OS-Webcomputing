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

<div class="wrapper-container">
<div class="wrapper2">

<p class="name-line"><span class="name">Patrick Radke</span></p>
<p class="name-line"> picture going here </p>
<p>-2nd Semester Computer Sience student at TH-Brandenburg</p>
<p>-working on the website development for this project</p>
</div>

<div class="wrapper3">
<p class="name-line"><span class="name">Julius Voigt</span></p>
<p class="name-line"> picture here </p>
<p>- 2nd Semester Computer Science student at TH-Brandenburg</p>
<p>- working on Snake-Game and Design for this project</p>
</div>
</div>

<div class="wrapper">
        <form action="../project.html" method="post">
            <button type="submit">back</button>
</div>
</main>
    <footer>
        <div class= "footer-logos">
            <a href="https://github.com/JuJu-Inf/Semester-Projekt-OS-Webcomputing" target="_blank" rel="noopener noreferrer">
                <img src="../images/GitHub_Logo.png" alt="GitHub logo" class="logo">
            </a>

            <a href="https://www.th-brandenburg.de/" target="_blank" rel="noopener noreferrer" class="logo-link">
                <img src="../images/THB_logo.png" alt="TH Brandenburg logo" class="logo">
            </a>

            <a href="http://pan.th-brandenburg.de/~radkep/cgi-bin/about-us.cgi" class="logo-link">
                <img src="../images/AboutUs_Logo.png" alt="About us logo" class="about-logo">
            </a>
        </div>
    </footer>
</body>
</html>""")
