# Übungen zu Listen Teil 2

vornamen = [
    "Anna", "Luca", "Emma", "Noah", "Mia",
    "Paul", "Lea", "Ben", "Sophie", "Elias",
    "Clara", "Leon", "Marie", "Jonas", "Lina",
    "Max", "Amelie", "Luis", "Hannah", "Felix",
    "Laura", "Tom", "Nina", "Jan", "Emily",
    "Tim", "Lena", "Finn", "Sara", "Moritz",
    "Julia", "Oskar", "Maja", "David", "Johanna",
    "Erik", "Isabel", "Simon", "Greta", "Fabian",
    "Antonia", "Philipp", "Helena", "Niklas", "Frida",
    "Theo", "Luisa", "Tobias", "Ella", "Matteo"
]

# 1. Schreibe eine for-Schleife, die alle Namen ausgibt, die länger als 4 Buchstaben sind
for n in vornamen:
  if len(n) > 4:
    print(n)

# 2. Erstelle eine Liste namen_mit_m
#    Schreibe dann eine for-Schleife, die alle Vornamen durchgeht und einen Namen dann zu namen_mit_m hinzufügt,
#    wenn der Namen mit "m" beginnt.
namen_mit_m = []
for n in vornamen:
  if n[0] == "M":
    namen_mit_m.append(n)
print("Namen mit 'm':", namen_mit_m)

# 3. Sortiere die Liste und gib sie aus
vornamen.sort()
print(vornamen)

# 3b. Sortiere die Liste rückwärts und gib sie aus
vornamen.sort(reverse=True)
print(vornamen)

# 4. Gib den Namen aus, der genau in der Mitte der Liste steht
print(vornamen[len(vornamen)//2])

# 5. Gib mit einer for-Schleife für jeden der Namen in der Liste kinder aus, ob er in der obigen Liste vornamen enthalten ist
#    z.B. "Hans ist NICHT enthalten"
kinder = ["Hans", "Luisa", "David", "Maria", "Christian", "Niklas"]
for n in kinder:
  if n in vornamen:
    print(f"{n} ist enthalten")
  else:
    print(f"{n} ist NICHT enthalten")
  
# 6. Erstelle eine leere Liste namens zufallszahlen. 
#    Schreibe eine for-Schleife, die 100 mal eine Zufallszahl zwischen -1000 und 1000 in die Liste einfügt (hier brauchst Du das random-Modul)
import random
zufallszahlen = []
for i in range(100):
  zufallszahlen.append(random.randint(-1000, 1000))
print("Zufallszahlen:", zufallszahlen)

# 6b. Schreibe eine for-Schleife, die das Maximum und das Minimum der Liste findet. Verwende dazu die Variablen maximum und minimum.
#     Gib am Ende Maximum und Minimum aus.
maximum, minimum = -1000, 1000  # Startwerte für max und min
for z in zufallszahlen:
  if z > maximum:
    maximum = z
  elif z < minimum:
    minimum = z
print(f"Maximum der Liste ist {maximum}, Minumum ist {minimum}")    
