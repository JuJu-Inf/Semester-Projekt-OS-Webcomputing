#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import html


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

<body class="about-us">
	<div class="header-row">
		<h1> About us</h1>
	</div>

<main>

<!-- a wrapper container holding both wrappers of this site for easy formatting -->

<div class="wrapper-container">

<div class="wrapper2">

	<p class="center-text"><span class="underline">Patrick Radke</span></p>
	<p>- 2nd Semester Computer Sience student at TH-Brandenburg</p>
	<p>- Matrikel Nr.: 20248227
	<p>- Website frontend/python script development for this project</p>
	<p>- <span class="underline">GitHub</span>:</p>
	<p><a href="https://github.com/JuJu-Inf" target="_blank" rel="noopener noreferrer">Patrick Radke / JuJu-Inf</a></p>

</div>

<div class="wrapper3">
	<p class="center-text"><span class="underline">Julius Voigt</span></p>
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
		<a href="https://github.com/JuJu-Inf/Semester-Projekt-OS-Webcomputing" target="_blank" rel="noopener noreferrer" class="logo-link">
		<img src="../images/GitHub_Logo.png" alt="GitHub logo" class="Git-logo">
		</a>

		<a href="https://www.th-brandenburg.de/" target="_blank" rel="noopener noreferrer" class="logo-link">
		<img src="../images/THB_logo.png" alt="TH Brandenburg logo" class="THB-logo">
		</a>

		<a href="about-us.cgi" class="logo-link">
		<img src="../images/AboutUs_Logo.png" alt="about us logo" class="About-logo">
		</a>
	</div>

</body>
</html>""")
