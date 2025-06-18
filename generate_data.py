
import csv
import random

# Données des villes
villes = [
    {"ville": "Abidjan", "lat": 5.348, "lon": -4.027},
    {"ville": "Bouaké", "lat": 7.683, "lon": -5.030},
    {"ville": "Yamoussoukro", "lat": 6.817, "lon": -5.283},
    {"ville": "San Pedro", "lat": 4.748, "lon": -6.640},
    {"ville": "Korhogo", "lat": 9.458, "lon": -5.629}
]

# Génération des données aléatoires
data = []
for ville in villes:
    precipitation = round(random.uniform(0, 100), 1)
    temp_min = round(random.uniform(20, 25), 1)
    temp_max = round(random.uniform(28, 36), 1)
    data.append([ville["ville"], ville["lat"], ville["lon"], precipitation, temp_min, temp_max])

# Écriture dans un fichier CSV
with open("donnees_meteo_ci.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Ville", "Latitude", "Longitude", "Precipitation", "Temp_Min", "Temp_Max"])
    writer.writerows(data)

print("✅ Fichier donnees_meteo_ci.csv généré avec succès.")
