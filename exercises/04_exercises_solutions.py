# Übungen zu Listen

# 1. Baue eine Liste mit mehreren Vornamen (Strings) und speichere sie unter dem Namen "vornamen"
vornamen = ["Hans", "Jeanne", "Isa", "Stefan", "Jacques"]

# 2. Gib den letzten der Vornamen aus, indem Du einen negativen Index verwendest.
print("Letzter:", vornamen[-1])

# 3. Schreibe eine for-Schleife, um alle Namen nacheinander auszugeben. Schreibe nach der Schleife: "Insgesamt <anzahl> Namen" und setze die passende Anzahl ein.
for n in vornamen:
  print(n)
print(f"Ingesamt {len(vornamen)} Namen")

# 4. Ersetze den dritten Vornamen durch "Peter"
vornamen[2] = "Peter"

# 5. Ersetze den letzten Vornamen durch "Maria"
vornamen[-1] = "Maria"

# 6. Hänge den Namen "Waltraud" an die Liste an
vornamen.append("Waltraud")

# 7. Füge den Namen "Aida" an der drittletzten Stelle ein
vornamen.insert(-3, "Aida")

# 8. Gib den Index von "Aida" in der Liste aus
print("Aida steht an Stelle", vornamen.index("Aida"))




