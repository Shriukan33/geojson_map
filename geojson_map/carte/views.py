from django.shortcuts import render
from django.views.generic import TemplateView

import folium
from pathlib import Path

# Create your views here.
class MainMapView(TemplateView):
    template_name = "carte/base.html"

    def __init__(self):
        self.build_map()

    def build_map(self, link=None):
        """
        Build a map centered on Nantes and adds a layer on it from either local file or link
        Result is stored in templates/cartes/map.html 
        """

        if link is not None:
            plan_theorie = str(link)
        else:
            plan_theorie = str(Path(__file__).resolve().parent / 'data' / 'planvelo-theorie.geojson') # Assuming the script is executed from the carte app

        m = folium.Map(location=[47.2184, -1.5556], zoom_start=12) # Centered on Nantes, can change the map style with the tiles argument
        folium.GeoJson(plan_theorie, name="geojson").add_to(m) # Adding the first layer of the map with the GeoJSON file

        folium.LayerControl().add_to(m) # Adds the option to filter Layers
        
        template_folder = str(Path(__file__).resolve().parent / 'templates' / 'carte')
        m.save(f"{template_folder}/map.html")

