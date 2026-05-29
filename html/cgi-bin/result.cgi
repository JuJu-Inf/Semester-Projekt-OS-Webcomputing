#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import html
import csv
import os
import cgitb

cgitb.enable()

#gives·.cgi·script·access·to·information·from·input·fields

form = cgi.FieldStorage()

action = form.getfirst("action", "").strip()

#stores·submitted·information,
#'html·escape'·converts·special·characters·(e.g.·<,·&)·to·HTML·safe·text,
#'.strip()'·removes·spaces·at·start·and·end·of·input

vorname_raw = form.getfirst("vorname", "").strip()
nachname_raw = form.getfirst("nachname", "").strip()
email_raw = form.getfirst("email", "").strip()
score_raw = form.getfirst("score", "0").strip()

#in·case·of·no·input

if vorname_raw == "":
	vorname_raw = "not given"
if nachname_raw == "":
	nachname_raw = "not given"
if email_raw == "":
	email_raw = "not given"

try:
	score_value = int(score_raw)
except ValueError:
	score_value = 0

csv_file = os.path.join(os.path.dirname(__file__), "scores.csv")

if not os.path.exists(csv_file):
	with open(csv_file, "w", newline="", encoding="utf-8") as f:
		writer = csv.writer(f)
		writer.writerow(["Vorname", "Nachname", "Email", "Score"])

if action == "reset":
	with open(csv_file, "w", newline="", encoding="utf-8") as f:
		writer = csv.writer(f)
		writer.writerow(["Vorname", "Nachname", "Email", "Score"])
else:
	with open(csv_file, "a", newline="", encoding="utf-8") as f:
		writer = csv.writer(f)
		writer.writerow([vorname_raw, nachname_raw, email_raw, score_value])

rows = []
with open(csv_file, "r", newline="", encoding="utf-8") as f:
	reader = csv.reader(f)
	rows = list(reader)

data_rows = rows[1:]
data_rows.sort(key=lambda row: int(row[3]), reverse=True)

vorname = html.escape(vorname_raw)
nachname = html.escape(nachname_raw)
email = html.escape(email_raw)
score = html.escape(str(score_value))

print("Content-Type: text/html; charset=utf-8")
print()

print(f"""<!DOCTYPE html>

<html lang="de">

<head>

	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Scoreboard</title>
	<link rel="stylesheet" href="../css/style.css" type="text/css">

</head>

<body class="result-page">

	<div class="header-row">
		<h1>Results</h1>
	</div>

	<div class="wrapper">
		<div class="current-result">
			<p><strong>last player:</strong> {vorname} </p>
			<p><strong>last score:</strong> {score}</p>

	</div>

	<div class="button-row">

		<form action="../project.html" method="get">
		<button type="submit">back to the start</button>
		</form>

<!--·sends·form·to·CGI·Python·script·and·method·=·"post"·sends·the·values·via·HTTP·Post-->

		<form action="result.cgi" method="post" onsubmit="return confirm('are you sure you want to reset the scoreboard?');">

		<input type="hidden" name="action" value="reset">
		<button type="submit">reset Scoreboard</button>
		</form>
	</div>

<table class="score-table">
	<tr>
		<th>Vorname</th>
		<th>Nachname</th>
		<th>Score</th>
	</tr>""")

#dont change the indentation until footer otherwise the reset function breaks completely

for row in data_rows:
    row_vorname = html.escape(row[0])
    row_nachname = html.escape(row[1])
    row_score = html.escape(row[3])

    print(f"""
	<tr>
		<td>{row_vorname}</td>
		<td>{row_nachname}</td>
		<td>{row_score}</td>
	</tr>""")

print("""
	</table>
	</div>

<footer>

<!--·Footer·for·THB-Logo,Github-repository·&·about-us·page-->

	<div class="footer-logos">
		<a href="https://github.com/JuJu-Inf/Semester-Projekt-OS-Webcomputing" target="_blank" rel="noopener noreferrer">
		<img src="../images/GitHub_Logo.png" alt="GitHub logo" class="Git-logo">
		</a>

		<a href="https://www.th-brandenburg.de/" target="_blank" rel="noopener noreferrer" class="logo-link">
		<img src="../images/THB_logo.png" alt="TH Brandenburg logo" class="THB-logo">
		</a>

		<a href="about-us.cgi" class="logo-link">
		<img src="../images/AboutUs_Logo.png" alt="about us logo" class="About-logo">
		</a>
	</div>
</footer>
</body>
</html>""")
