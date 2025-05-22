# Übungen zu Operatoren

# 1. Wende auf die Werte a und b die folgenden Operatoren an: +, -, *, /, // , **, % 
# Gib die Rechnung und das Ergebnis mit print und einem f-String aus.
a = 10
b = 5
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")
print(f"{a} % {b} = {a % b}")

# 2. Erweitere den Code aus 1. und schreibe den Typ des Ergebnisses dahinter.
# Beispiel: 10 / 2 = 5.0 (Typ float)

print(f"{a} + {b} = {a + b} (Typ {type(a + b)})")
print(f"{a} - {b} = {a - b} (Typ {type(a - b)})")
print(f"{a} * {b} = {a * b} (Typ {type(a * b)})")
print(f"{a} / {b} = {a / b} (Typ {type(a / b)})")
print(f"{a} // {b} = {a // b} (Typ {type(a // b)})")
print(f"{a} ** {b} = {a ** b} (Typ {type(a ** b)})")
print(f"{a} % {b} = {a % b} (Typ {type(a % b)})")

# Übungen zu if/else/elif

# 1. Frage den Benutzer mit input nach seinem Lieblingstier. Falls die Eingabe != "Elefant" ist, soll 
# das Programm antworten "Ah, Dein Lieblingstier ist <eingabe>. Meines ist der Elefant.".
# Wenn der Benutzer "Elefant" eingegeben hat, soll das Progamm mit "Cool, meins auch!!" antworten.

eingabe = input("Was ist Dein Lieblingstier? ")
if eingabe == "Elefant":
  print("Cool, meins auch!!")
else:
  print(f"Ah, Dein Lieblingstier ist also {eingabe}. Meines ist der Elefant.")

# 1b. Verwende eine Variable für das Lieblingstier des Computers. Passe den Code entsprechend an.
computer_lieblingstier = "Ente"
eingabe = input("Was ist Dein Lieblingstier? ")
if eingabe == computer_lieblingstier:
  print("Cool, meins auch!!")
else:
  print(f"Ah, Dein Lieblingstier ist also {eingabe}. Meines ist der/die/das {computer_lieblingstier}.")

# 2. Frage den Benutzer nach einer Zahl. Wandle die Eingabe in einen int um.
# Anschließend prüfst Du (if/elif/else), ob die Zahl durch 5 UND durch 3 teilbar ist, oder nur durch 5, 
# oder nur durch 3, oder keines von beiden. Gib das Ergebnis entsprechend aus.
zahl = int(input("Sag eine Zahl: "))
if zahl % 5 == 0 and zahl % 3 == 0:
  print(f"{zahl} ist sowohl durch 5 als auch durch 3 teilbar!")
elif zahl % 5 == 0:
  print(f"{zahl} ist durch 5 teilbar!")
elif zahl % 3 == 0:
  print(f"{zahl} ist durch 3 teilbar!")
else:
  print(f"{zahl} ist weder durch 5 noch durch 3 teilbar!")

# 3. Schreibe das Spiel Zahlenraten mit Hilfe einer while-Schleife. Der Benutzer muss eine zufällige Zahl raten.
# Hierfür verwenden wir das Python-Modul "random", um mit der Funktion "randint" einen Zufalls-Integer zwischen
# 1 und 10000 zu ermitteln.
import random 
secret = random.randint(1, 10000)
# Schreibe nun eine while-Schleife, die vom Benutzer einen Rateversuch abfragt und mit "Größer" / "Kleiner" / "Korrekt" reagiert.
# Beim Erraten soll die Schleife abbrechen.
# Denk an die Umwandlung der Eingabe in einen int!
while True:
  rateversuch = int(input("Rate meine Zahl: "))
  if rateversuch > secret:
    print("Kleiner")
  elif rateversuch < secret:
    print("Größer")
  else:
    print("Korrekt")
    break

# 4. Erweitere das Spiel um einen Test, ob der Benutzer um 1 daneben liegt. Wenn ja, soll "fast richtig ..." ausgegeben werden. 
secret = random.randint(1, 10000)
# Schreibe nun eine while-Schleife, die vom Benutzer einen Rateversuch abfragt und mit "Größer" / "Kleiner" / "Korrekt" reagiert.
# Beim Erraten soll die Schleife abbrechen.
# Denk an die Umwandlung der Eingabe in einen int!
while True:
  rateversuch = int(input("Rate meine Zahl: "))
  if rateversuch > secret:
    print("Kleiner")
  elif rateversuch < secret:
    print("Größer")
  else:
    print("Korrekt")
    break
  
  if rateversuch + 1 == secret or rateversuch - 1 == secret:
    print("Aber fast richtig ...")
