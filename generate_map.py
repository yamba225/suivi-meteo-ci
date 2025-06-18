
import pandas as pd
import folium

# Chargement des données CSV
df = pd.read_csv("donnees_meteo_ci.csv")

# Création de la carte
carte = folium.Map(location=[7.5, -5.0], zoom_start=6)

# Ajout des marqueurs avec popup
for _, row in df.iterrows():
    popup_content = f"""
    <b>Ville :</b> {row['Ville']}<br>
    🌧️ <b>Précipitations :</b> {row['Precipitation']} mm<br>
    🌡️ <b>Temp. min :</b> {row['Temp_Min']} °C<br>
    🔥 <b>Temp. max :</b> {row['Temp_Max']} °C
    """
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=popup_content,
        icon=folium.Icon(color="blue", icon="cloud")
    ).add_to(carte)

# Sauvegarde de la carte
carte.save("carte_meteo_ci.html")
print("✅ Carte carte_meteo_ci.html générée avec succès.")
