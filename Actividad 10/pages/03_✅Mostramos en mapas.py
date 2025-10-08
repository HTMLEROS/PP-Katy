import folium
import streamlit as st
from streamlit_folium import folium_static, st_folium
import pandas as pd

def generar_mapa():
    attr = (
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> '
        'contributors, &copy; <a href="https://cartodb.com/attributions">CartoDB</a>'
    )
    
    tiles = 'https://wms.ign.gob.ar/geoserver/gwc/service/tms/1.0.0/capabaseargenmap@EPSG%3A3857@png/{z}/{x}/{-y}.png'
    m = folium.Map(
        location=(-33.457606, -65.346857),
        control_scale=True,
        zoom_start=5,
        name='es',
        tiles=tiles,
        attr=attr
    )
    return m


precios = pd.read_csv('precios.csv')
precios = precios.dropna(subset=["latitud","longitud"])
st.title("Mapa")
mapa = generar_mapa()

def agregar_marca_aerop(row):
    
    #st.write(color)
    folium.Marker(
        [row['latitud'], row['longitud']],
        popup=row['producto'],
        icon=folium.Icon()
        ).add_to(mapa)

ac1,ac2 = st.columns([0.3, 0.7])
r_GasOilGrado2 = ac1.checkbox("Gas Oil Grado 2")
if r_GasOilGrado2:
    a_larg = precios[precios['producto']=='Gas Oil Grado 2']
    a_larg.apply(agregar_marca_aerop, axis=1)
r_GasOilGrado3= ac1.checkbox("Gas Oil Grado 3")
if r_GasOilGrado3:
    a_med = precios[precios['producto']=='Gas Oil Grado 3']
    a_med.apply(agregar_marca_aerop, axis=1)

with ac2:
    st_folium(mapa, key='precios')
