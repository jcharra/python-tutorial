# TIC TAC TOE
#
# Dies ist eine umfangreichere Übung, bei der Du Dein gesamtes bisheriges Wissen einbringen kannst: 
# Wir programmieren den Klassiker Tic-Tac-Toe als interaktives Spiel.

# Lege das Spielfeld als Liste von neun Feldern an. Ein leeres Feld soll einfach ein Leerzeichen sein.
feld = ["_"] * 9

# Wir brauchen eine Variable "winner", die am Anfang der leere String ist.
# Wir brauchen eine Variable "player", die das Symbol (x / o) des Spielers enthält, der dran ist.
# Das Spiel selbst läuft als while-Schleife, bis ein Spieler gewonnen hat. 

winner = ""
player = "x"
while True:
  # Gib das Spielfeld mit print aus (hier brauchst Du eine for-Schleife)
  for i in range(9):
    if i % 3 == 0:
      print("")
    print(feld[i], end="")
  
  if winner:
    print(f"\n\nDer Gewinner ist Spieler '{winner}'. Glückwunsch! \n\n")
    break
      
  # Frage den Benutzer nach dem nächsten Zug (Zahl von 1 bis 9 bzw. 0 bis 8)
  idx = int(input("\n\nNächster Zug? "))
  
  # Falls das Feld belegt ist, gib "Feld bereits belegt aus" und wiederhole die Frage (continue)
  if feld[idx] != "_":
    print("Feld bereits belegt!")
    continue
  
  # Füge den Zug als "x" oder "o" ein, je nachdem wer grade dran ist.
  feld[idx] = player
  
  # Spielerwechsel
  if player == "x":
    player = "o"
  else:
    player = "x"
    
  for winning in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
    a, b, c = winning
    if feld[a] != "_" and feld[a] == feld[b] and feld[b] == feld[c]:
      winner = feld[a]
      break

  