import pandas as pd
import streamlit as st

precios =  pd.read_csv('precios.csv')
st.title("Parte 1")
st.header("Datos que encontraron")
filas, columnas = precios.shape
with st.expander("¿Cuántas filas y columnas tiene el dataset?"):
    filas, columnas = precios.shape
    st.write(f'Tiene { precios} filas y {precios} columnas')
    
    
nombres_ubic = precios['tipohorario'].unique()
cant_ubic = len(precios['tipohorario'].unique())

with st.expander("¿Cuántos son los valores únicos de la columna **tipohorario**?"):
    st.write(cant_ubic)
with st.expander("¿Cuáles son los valores únicos de la columna **tipohorario**?"):
    st.write(nombres_ubic)
with st.expander("¿Cuáles son los nombres de las columnas  precios?"):
   
    st.write(precios.columns)

        
