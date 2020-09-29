function f1(){ document.getElementById("show_frage").innerHTML="Wie hiesst der Prozessor des SNES?"; a = "W65C816S";}
function f2(){ document.getElementById("show_frage").innerHTML="Wie hiesst die Verschlüsselungsmaschine der Wehrmacht?"; a = "Enigma";}
function f3(){ document.getElementById("show_frage").innerHTML="Was für ein Protokol wird für sichere Kommunikation im Internet verwendet?"; a = "HTTPS";}
function f4(){ document.getElementById("show_frage").innerHTML="Wie wird das Logische OR auch gennant?"; a = "Disjunktion";}
function f5(){ document.getElementById("show_frage").innerHTML="Wie wird das logische AND auch genannt"; a = "Konjunktion";}
function f6(){ document.getElementById("show_frage").innerHTML="Ist HTML eine Programmiersprache?"; a = "Nein";}
function f7(){ document.getElementById("show_frage").innerHTML="Ist Java und Javascript dasselbe?"; a = "Nein";}
function f8(){ document.getElementById("show_frage").innerHTML="Welche Programmiersprache wurde für diese Webseite verwendet?"; a = "Javascript";}

answer = ''

function calc() {
	answer = document.getElementById('answer');
	if (a == antwort) {
		document.getElementById("show_frage").innerHTML="Richtig";
	}
	else{
		document.getElementById("show_frage").innerHTML="Falsch";
	}
}