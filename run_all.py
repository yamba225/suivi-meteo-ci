
import subprocess

print("🟡 Génération du fichier de données météo...")
subprocess.run(["python", "generate_data.py"])

print("🟡 Génération de la carte interactive...")
subprocess.run(["python", "generate_map.py"])

print("✅ Tous les fichiers ont été générés avec succès.")
