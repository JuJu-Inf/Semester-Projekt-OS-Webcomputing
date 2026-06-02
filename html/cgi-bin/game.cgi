#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import html
import urllib.parse

#gives .cgi script access to information from input fields

form = cgi.FieldStorage()

#stores submitted information,
#'html escape' converts special characters (e.g. <, &) to HTML safe text,
#'.strip()' removes spaces at start and end of input

vorname = html.escape(form.getfirst("vorname", "").strip())
nachname = html.escape(form.getfirst("nachname", "").strip())
snake_color = form.getfirst("snakeColor", "").strip()

if vorname == "":
	vorname = "not given"
if nachname == "":
	nachname = "not given"
if snake_color  == "":
	snake_color = "#579934"

snake_color_url = urllib.parse.quote(snake_color)

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
		<h1>Arcade Game</h1>
	</div>

	<div class="game-wrapper">
		<iframe id="snakeFrame" src="../game/game-file.html?snakeColor={snake_color_url}" width="820" height="820" scrolling="no" title="Snake Game"></iframe>

	<div class="score">
		<h2>Score</h2>
		<p id="scoreDisplay">0</p>
		<button type="button" id="pauseButton">Pause</button>
	</div>
	</div>

		<form id="resultForm" action="result.cgi" method="post">
			<input type="hidden" name="vorname" value="{vorname}">
			<input type="hidden" name="nachname" value="{nachname}">
			<input type="hidden" name="score" id="scoreInput" value="0">
		</form>


<footer>

	<div class="footer-logos">
		<a href="https://github.com/JuJu-Inf/Semester-Projekt-OS-Webcomputing" target="_blank" rel="noopener noreferrer">
		<img src="../images/GitHub_Logo.png" alt="GitHub logo" class="Git-logo">
		</a>

		<a href="https://www.th-brandenburg.de/" target="_blank" rel="noopener noreferrer" class="logo-link">
		<img src="../images/THB_logo.png" alt="TH Brandenburg logo" class="THB-logo">
		</a>

		<a href="about-us.cgi" class="logo-link">
		<img src="../images/AboutUs_Logo.png" alt="About us logo" class="About-logo">
		</a>
	</div>
</footer>

<!-- script processing the information that is being sent by the game-file & pausbutton logic -->

<script>

const pauseButton = document.getElementById("pauseButton");
const snakeFrame = document.getElementById("snakeFrame");

let paused = false;

	pauseButton.addEventListener("click", function () {{

		document.getElementById("snakeFrame").contentWindow.postMessage({{ type: "togglePause" }}, "*");
		paused = !paused;
		pauseButton.textContent = paused ? "Resume" : "Pause";

		setTimeout(function() {{
			snakeFrame.focus();
			snakeFrame.contentWindow.focus();
		}}, 0);
	}});

	window.addEventListener("message", function(event) {{

		if (!event.data || typeof event.data !== "object") return;

		if (event.data.type === "scoreUpdate") {{
			const latestScore = Number(event.data.score) || 0;
			document.getElementById("scoreDisplay").textContent = latestScore;
		}}

		if (event.data.type === "gameOver") {{
			const latestScore = Number(event.data.score) || 0;
			document.getElementById("scoreDisplay").textContent = latestScore;

<!--·update·'invisible'·score·counter,·given·to·result.cgi to print Scoreboard entry·-->

			document.getElementById("scoreInput").value = latestScore;

			const retry = confirm
				("Game Over!\\n Your score: " + latestScore + " \\n \\n OK = Play again \\n Cancel = proceed to Scoreboard");

<!-- the confirm func. only gives back a true (Ok) or flase (cancel) hence the simple if/else function  -->

		if (retry) {{
		document.getElementById("snakeFrame").contentWindow.postMessage({{ type: "restartGame" }}, "*");
		}}

		else {{
			document.getElementById("resultForm").submit();
		}}
		}}
	}});
</script>

<!-- using doubled braces here since we're printing the script in a f string from python, if using single braces python would interpret it wrong (not as JS) -->

</body>
</html>""")
