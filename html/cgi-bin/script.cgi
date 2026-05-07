#!/usr/bin/env python3

import cgi
import html

form = cgi.FieldStorage()

vorname = form.getfirst("vorname", "").strip()
nachname = form.getfirst("nachname", "").strip()
email = form.getfirst("email", "").strip()

if vorname == "":
    vorname = "not given"
if nachname == "":
    nachname = "not given"
if email == "":
    email = "not given"

vorname = html.escape(vorname)
nachname = html.escape(nachname)
email = html.escape(email)

print("Content-Type: text/html; charset=utf-8")
print()

print(f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Übermittelte Daten</title>
    <link rel="stylesheet" href="../css/style.css" type="text/css">
</head>
<body>
    <div class="header-row">
        <a href="https://www.th-brandenburg.de/" target="_blank" rel="noopener noreferrer" class="logo-link">
            <img src="../images/THB_logo.png" alt="TH Brandenburg logo" class="logo">
        </a>

        <h1>Übermittelte Daten</h1>
    </div>

    <div class="wrapper">
        <p><strong>Vorname:</strong> {vorname}</p>
        <p><strong>Nachname:</strong> {nachname}</p>
        <p><strong>Email:</strong> {email}</p>

        <p><a href="../project.html">Zurück zum Formular</a></p>
    </div>

    <footer>
        <p>
            <a href="https://github.com/JuJu-Inf/Semester-Projekt-OS-Webcomputing" target="_blank" rel="noopener noreferrer">
                Zum GitHub Repository
            </a>
        </p>
    </footer>
</body>
</html>""")
