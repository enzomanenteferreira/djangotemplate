from django.shortcuts import render, redirect
import folium
from django.db import connection
import pandas as pd
import geopandas as gpd
import geemap
import os
import ee

# Create your views here.

def home(request):
    sql = """ SELECT * FROM linha1"""

    sql2 = """SELECT * FROM poligono1"""

    sql3  = """SELECT * FROM nyc_neighborhoods"""

    gdf = gpd.read_postgis(sql,connection)
    #gdf2 = gpd.read_postgis(sql2,connection)
    #gdf3 = gpd.read_postgis(sql3, connection)
    
    m = geemap.Map(center=[-3.13376, -51.77645], zoom=13)

    #mapa hybrid google basemap
    os.environ["HYBRID"] = 'https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}'

    #adicionar basemaps
    m.add_basemap("Esri.WorldImagery")
    m.add_basemap("HYBRID")
    #converter o mapa para html
    html_str = m.to_html()

    context = {'my_map': html_str}
    return render(request, 'geoApp/home.html', context)







def teste(request):


    return render(request, 'geoApp/teste.html')