# 🌍 Suivi Météo Côte d'Ivoire

Ce projet permet de générer automatiquement une carte interactive affichant les précipitation, les températures minimales et smaximales de quelques villes de la Côte d’Ivoire.
---

## 📁 Contenu du projet

| Fichier | Description |
|--------|-------------|
| `generate_data.py` | Génère un fichier CSV avec des données météo simulées |
| `generate_map.py` | Crée une carte HTML à partir du fichier CSV |
| `run_all.py` | Exécute automatiquement les deux scripts ci-dessus |
| `donnees_meteo_ci.csv` | Données météo (exemple généré automatiquement) |
| `carte_meteo_ci.html` | Carte interactive générée avec Folium |
| `index.html` | Page web intégrant la carte via iframe (prête pour GitHub Pages) |

---

## ▶️ Instructions d’utilisation

### 🔧 1. Installer les dépendances

Assurez-vous d’avoir Python 3.7+ installé.

Installez les bibliothèques nécessaires :
```bash

pip install pandas folium

````

### ⚙️ 2. Générer les fichiers automatiquement

Exécutez le script principal :

```bash

python run_all.py
```

Ce script :

* génère le fichier `donnees_meteo_ci.csv`
* crée la carte interactive `carte_meteo_ci.html`



---

## ✨ Résultat

Une carte interactive affichant :

* 🌧️ Précipitations (mm)
* 🌡️ Température minimale (°C)
* 🔥 Température maximale (°C)

---

## 📌 Remarques

* Les données sont générées aléatoirement pour démonstration.
* Vous pouvez modifier les villes ou plages de température dans `generate_data.py`.

---

## 🧑‍💻 Auteur

Ce projet a été généré par Yamba Otobou Gnagne Dominique pour un usage éducatif ou personnel.





suivi-meteo-ci/
├── generate_data.py          # Script : génère les données météo CSV
├── generate_map.py           # Script : crée la carte HTML avec Folium
├── run_all.py                # Script principal automatisé
├── donnees_meteo_ci.csv      # Données météo (exemple)
├── carte_meteo_ci.html       # Carte HTML générée
├── index.html                # Page web d'accueil (GitHub Pages)
└── README.md                 # Guide complet d'utilisation
