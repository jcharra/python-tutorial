# Übungen zu range

# 1. Gib eine Liste aller Zahlen von 1 bis 100 aus
print(list(range(1, 101)))

# 2. Gib eine Liste aller ungeraden Zahlen von 1 bis 999 aus
print(list(range(1, 1000, 2)))

# 3. Gib eine Liste mit Zahlen von 1000 bis einschließlich 100 aus, rückwärts in 10er-Schritten
print(list(range(1000, 99, -10)))

# Übungen zu for / range

# 1. Frage den Benutzer nach zwei Zahlen a und b.
# Gib anschließend alle Zahlen von a bis b in einer for-Schleife aus.
a = int(input("Erste Zahl: "))
b = int(input("Zweite Zahl: "))
print(list(range(a, b)))

# 2. Frage den Benutzer nach zwei Zahlen a und b. 
# Gib dann die Summe aller Zahlen von a bis einschließlich (!) b aus.
a = int(input("Erste Zahl: "))
b = int(input("Zweite Zahl: "))
sum = 0
for i in range(a, b + 1):
  sum += i
print("Die Summe ist", sum)

# 3. Frage den Benutzer nach einer Zahl z.
# Prüfe mit einer for-Schleife, ob es eine Primzahl ist.
# Gib entweder "Primzahl" aus, oder "Teilbar durch x", wenn Du einen Teiler x gefunden hast.
# Überlege Dir, bis zu welcher Zahl Deine for-Schleife Teiler prüfen muss. Kannst Du hier optimieren?
isPrime = True
x = int(input("Welche Zahl soll ich prüfen? "))

# Die for-Schleife läuft bis einschließlich zur WURZEL von x. 
# Wenn man nämlich bis dahin keinen Teiler gefunden hat, findet man
# jenseits der Wurzel auch keinen mehr!
# Beachte die folgenden Details: 
# x hoch 0.5 ergibt die Wurzel. 
# Man muss das Ergebnis zu einem int konvertieren, weil range keine float-Werte akzeptiert.
# Man muss zu dem Wert noch +1 rechnen, weil die obere Grenze nicht im range enthalten ist.
for i in range(2, int(x ** 0.5) + 1):
  if x % i == 0:
    print(f"Keine Primzahl. {x} ist teilbar durch {i}")
    isPrime = False
    break

if isPrime:
  print("Primzahl")

# Alternative Lösung: Speichere den größten Teiler. Wenn der am Ende =1 ist, ist es eine Primzahl.
divisor = 1
x = int(input("Welche Zahl soll ich prüfen? "))
for i in range(2, int(x ** 0.5) + 1):
  if x % i == 0:
    # Teiler gefunden => speichern und abbrechen
    divisor = i
    break

if divisor == 1:
  print("Primzahl")
else:
  print(f"Keine Primzahl. {x} ist teilbar durch {divisor}")
