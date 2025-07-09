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

# 2. Erstelle eine Liste namen_mit_m
#    Schreibe dann eine for-Schleife, die alle Vornamen durchgeht und einen Namen dann zu namen_mit_m hinzufügt,
#    wenn der Namen mit "m" beginnt.

# 3. Sortiere die Liste und gib sie aus

# 3b. Sortiere die Liste rückwärts und gib sie aus

# 4. Gib den Namen aus, der genau in der Mitte der Liste steht

# 5. Gib mit einer for-Schleife für jeden der Namen in der Liste kinder aus, ob er in der obigen Liste vornamen enthalten ist
#    z.B. "Hans ist NICHT enthalten"
kinder = ["Hans", "Luisa", "David", "Maria", "Christian", "Niklas"]

# 6. Erstelle eine leere Liste namens zufallszahlen. 
#    Schreibe eine for-Schleife, die 100 mal eine Zufallszahl zwischen -1000 und 1000 in die Liste einfügt (hier brauchst Du das random-Modul)
# import random
# random.randint(-1000, 1000)

# 6b. Schreibe eine for-Schleife, die das Maximum und das Minimum der Liste findet. Verwende dazu die Variablen maximum und minimum.
#     Gib am Ende Maximum und Minimum aus.
maximum, minimum = -1000, 1000  # Startwerte für max und min