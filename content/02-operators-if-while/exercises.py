# Übungen zu if/else/elif

# 1. Frage den Benutzer mit input nach seinem Lieblingstier. Falls die Eingabe != "Elefant" ist, soll 
# das Programm antworten "Ah, Dein Lieblingstier ist <eingabe>. Meines ist der Elefant.".
# Wenn der Benutzer "Elefant" eingegeben hat, soll das Progamm mit "Cool, meins auch!!" antworten.


# 1b. Verwende eine Variable für das Lieblingstier des Computers. Passe den Code entsprechend an.


# 2. Frage den Benutzer nach einer Zahl. Wandle die Eingabe in einen int um.
# Anschließend prüfst Du (if/elif/else), ob die Zahl durch 5 UND durch 3 teilbar ist, oder nur durch 5, 
# oder nur durch 3, oder keines von beiden. Gib das Ergebnis entsprechend aus.


# 3. Schreibe das Spiel Zahlenraten mit Hilfe einer while-Schleife. Der Benutzer muss eine zufällige Zahl raten.
# Hierfür verwenden wir das Python-Modul "random", um mit der Funktion "randint" einen Zufalls-Integer zwischen
# 1 und 10000 zu ermitteln.
import random 
secret = random.randint(1, 10000)
# Schreibe nun eine while-Schleife, die vom Benutzer einen Rateversuch abfragt und mit "Größer" / "Kleiner" / "Korrekt" reagiert.
# Beim Erraten soll die Schleife abbrechen.
# Denk an die Umwandlung der Eingabe in einen int!

# 4. Erweitere das Spiel um einen Test, ob der Benutzer um 1 daneben liegt. Wenn ja, soll "fast richtig ..." ausgegeben werden. 
