#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

<body class="game-page">
    	<div class="header-row">
        	<h1>Snake Game</h1>
    	</div>

    	<div class="game-wrapper">
        	<iframe id="snakeFrame" src="../game/game-file.html" width="820" height="820" scrolling="no" title="Snake Game"></iframe>

        <div class="score">
            	<h2>Score</h2>
            	<p id="scoreDisplay">0</p>
        </div>
    	</div>

    	<div class="wrapper">
        	<form id="resultForm" action="result.cgi" method="post">
            		<input type="hidden" name="vorname" value="{vorname}">
            		<input type="hidden" name="nachname" value="{nachname}">
            		<input type="hidden" name="email" value="{email}">
            		<input type="hidden" name="score" id="scoreInput" value="0">
            	<button type="submit">Weiter zur Auswertung</button>
        	</form>
    	</div>

<footer>
        <div class="footer-logos">
            	<a href="https://github.com/JuJu-Inf/Semester-Projekt-OS-Webcomputing" target="_blank" rel="noopener noreferrer">
                <img src="../images/GitHub_Logo.png" alt="GitHub logo" class="Git-logo">
            	</a>

<!-- Footer for THB-Logo,Github-repository & about-us page-->            

		<a href="https://www.th-brandenburg.de/" target="_blank" rel="noopener noreferrer" class="logo-link">
                <img src="../images/THB_logo.png" alt="TH Brandenburg logo" class="THB-logo">
            	</a>
            	
		<a href="about-us.cgi" class="logo-link">
                <img src="../images/AboutUs_Logo.png" alt="About us logo" class="About-logo">
            	</a>
        /div>
</footer>

<script>
	window.addEventListener("message", function(event) {{
            if (!event.data || typeof event.data !== "object") return;

            if (event.data.type === "scoreUpdate") {{
            	const latestScore = Number(event.data.score) || 0;
            	document.getElementById("scoreDisplay").textContent = latestScore;
            	document.getElementById("scoreInput").value = latestScore;
            }}

            if (event.data.type === "gameOver") {{
            	const latestScore = Number(event.data.score) || 0;
            	document.getElementById("scoreDisplay").textContent = latestScore;
            	document.getElementById("scoreInput").value = latestScore;

                const retry = confirm("Game Over!\\nDein Score: " + latestScore + "\\n\\nOK = Nochmal spielen\\nAbbrechen = Zur Scoreboard-Seite");

            if (retry) {{
            	document.getElementById("snakeFrame").contentWindow.postMessage({{ type: "restartGame" }}, "*");
            }} 
	    
		else {{
                	document.getElementById("resultForm").submit();
                }}
            }}
        }});
</script>

<!-- using doubled braces here since we're printing the script in a f string from python, if using single braces python would interpret it wrong (not as JS)-->

</body>
</html>""")
