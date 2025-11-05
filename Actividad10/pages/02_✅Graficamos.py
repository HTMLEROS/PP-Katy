import streamlit as st
import pandas as pd

import streamlit as st
import matplotlib.pyplot as plt


precios = pd.read_csv('precios.csv')
st.title("Gráfico")
fig,ax = plt.subplots()
# Crear el gráfico de barras
conteo_tipos = precios['provincia'].value_counts()
conteo_tipos.plot(kind='bar', ax=ax, color='skyblue')
# Agregar etiquetas y título
ax.set_xlabel('provincias')
ax.set_ylabel('Cantidad')
ax.set_title('Cantidad de provincia por tipohorario ')

# Mostrar el gráfico
st.pyplot(fig)
