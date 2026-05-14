#!/usr/bin/env python3

import cgi
import html

form = cgi.FieldStorage()

vorname = html.escape(form.getfirst("vorname", "").strip())
nachname = html.escape(form.getfirst("nachname", "").strip())
email = html.escape(form.getfirst("email", "").strip())

if vorname == "":
    vorname = "not given"
if nachname == "":
    nachname = "not given"
if email == "":
    email = "not given"

print("Content-Type: text/html; charset=utf-8")
print()

print(f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Snake Game</title>
    <link rel="stylesheet" href="../css/style.css" type="text/css">
</head>
<body>
    <div class="header-row">
	<h1> Snake Game </h1>
    </div>

    <div class="game-wrapper">
        <iframe src="../game_tests/test_game_in_Website.html" width="1050" height="1150" title="Snake Game"></iframe>

    </div>

    <div class="wrapper">
        <form action="result.cgi" method="post">
            <input type="hidden" name="vorname" value="{vorname}">
            <input type="hidden" name="nachname" value="{nachname}">
            <input type="hidden" name="email" value="{email}">
            <button type="submit">Weiter zur Auswertung</button>
        </form>
    </div>

    <footer>
         <div class= "footer-logos">
            <a href="https://github.com/JuJu-Inf/Semester-Projekt-OS-Webcomputing" target="_blank" rel="noopener noreferrer">
              <img  src="../images/GitHub_Logo.png" alt="TH Brandenburg logo" class="logo">
          </a>
            <a href="https://www.th-brandenburg.de/" target="_blank" rel="noopener noreferrer" class="logo-link">
              <img src="../images/THB_logo.png" alt="TH Brandenburg logo" class="logo">
          </a>
            <a href="http://pan.th-brandenburg.de/~radkep/cgi-bin/about-us.cgi" class="logo-link">
              <img src="../images/THB_logo.png" alt="about us logo" class="about-logo">
          </a>
        </div>
    </footer>
</body>
</html>""")
