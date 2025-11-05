import pandas as pd
import streamlit as st

precios =  pd.read_csv('precios.csv')
st.titles("Parte 1")
st.header("en esta aplicasion nos hiciernon hacer preguntas y respuestas de y a mi se me ocurrior poner lo mas importante del dato que me toco como algunos productos que tenia mas mensionados y otra de las cosas saber que puede interesar como los nombres de cada columnas que tiene mi datos")
st.header("Datos que encontraron")
filas, columnas = precios.shape
with st.expander("¿Cuántas filas y columnas tiene el dataset?"):
    filas, columnas = precios.shape
    st.write(f'Tiene { precios} filas y {precios} columnas')
    
    
nombres_ubic = precios['producto'].unique()
cant_ubic = len(precios['producto'].unique())

with st.expander("¿Cuántos son los valores únicos de la columna **producto**?"):
    st.write(cant_ubic)
with st.expander("¿Cuáles son los valores únicos de la columna **producto**?"):
    st.write(nombres_ubic)
with st.expander("¿Cuáles son los nombres de las columnas  precios?"):
   
    st.write(precios.columns)

        
