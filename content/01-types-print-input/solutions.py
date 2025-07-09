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

# 3. Weise den Variablen a, b, c und d vier beliebige Werte zu, indem Du nur eine einzige Zeile Code verwendest. 
#    Gib die vier Werte anschließend mit print aus.
a, b, c, d = 10, "Hallo", 4.5, True
print(a, b, c, d)

# 4. Frage den Benutzer nach seinem Namen. Gib anschließend "Hallo, <name>" aus.
name = input("Wie heißt Du?")
print(f"Hallo {name}!")