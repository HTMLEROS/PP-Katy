import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

redes =  pd.read_csv('uso_digitales_FINAL.csv')
st.title("Parte 1")
st.header("En esta parte verás unos datos de una encuesta que se realizó a los jóvenes de la técnica 9 en el año pasado y en el año anterior, sobre las aplicasiones que usaban más")
st.header("Datos que encontraron")
filas, columnas = redes.shape
with st.expander("¿Cuántas filas y columnas tiene el dataset?"):
    filas, columnas = redes.shape
    st.write(f'Tiene { redes} filas y {redes} columnas')
    
    
nombres_ubic = redes['Género'].unique()
cant_ubic = len(redes['Marcá las redes sociales que utilizás'].unique())
nombres_ubic = redes['Edad'].unique()

with st.expander("¿Cuántos son los valores únicos de la columna **Marcá las redes sociales que utilizás**?"):
    st.write(cant_ubic)
with st.expander("¿Cuáles son los valores únicos de la columna **Género**?"):
    st.write(nombres_ubic)
with st.expander("¿Cuáles son los valores únicos de la columna **Edad**?"):
    st.write(nombres_ubic)
with st.expander("¿Cuáles son los nombres de las columnas  redes?"):
   
    st.write(redes.columns)
st.image('images/aplicacion.png')
st.header("Estas imagenes que vez son algunas aplicaciónes más votados en la información de la encuesta")


redes= pd.read_csv('uso_digitales_FINAL.csv')
st.title("Gráfico")
fig,ax = plt.subplots()
# Crear el gráfico de barras
conteo_tipos = redes['instagram'].value_counts()
conteo_tipos.plot(kind='bar', ax=ax, color='skyblue')
# Agregar etiquetas y título
ax.set_xlabel('Género')
ax.set_ylabel('Cantidad')
ax.set_title('la cantidad de horas que usaron cada uno intagram ')

# Mostrar el gráfico
st.pyplot(fig)       

redes= pd.read_csv('uso_digitales_FINAL.csv')
fig,ax = plt.subplots()
# Crear el gráfico de barras
conteo_tipos = redes['tiktok'].value_counts()
conteo_tipos.plot(kind='bar', ax=ax, color='skyblue')
# Agregar etiquetas y título
ax.set_xlabel('Género')
ax.set_ylabel('Cantidad')
ax.set_title('la cantidad de horas que usaron cada uno tiktok ')

# Mostrar el gráfico
st.pyplot(fig)       

redes= pd.read_csv('uso_digitales_FINAL.csv')
fig,ax = plt.subplots()
# Crear el gráfico de barras
conteo_tipos = redes['youtube'].value_counts()
conteo_tipos.plot(kind='bar', ax=ax, color='skyblue')
# Agregar etiquetas y título
ax.set_xlabel('Género')
ax.set_ylabel('Cantidad')
ax.set_title('la cantidad de horas que usaron cada uno youtube ')

# Mostrar el gráfico
st.pyplot(fig)       

redes= pd.read_csv('uso_digitales_FINAL.csv')
fig,ax = plt.subplots()
# Crear el gráfico de barras
conteo_tipos = redes['twiter'].value_counts()
conteo_tipos.plot(kind='bar', ax=ax, color='skyblue')
# Agregar etiquetas y título
ax.set_xlabel('Género')
ax.set_ylabel('Cantidad')
ax.set_title('la cantidad de horas que usaron cada uno twiter ')

# Mostrar el gráfico
st.pyplot(fig)       