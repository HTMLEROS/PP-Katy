import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("información  de precios de nafta")
st.header("La información que obtienen en este archivo  son algunos precios que de naftas ,horario de atención nocturno y de dia como tambien los tipos de gasolina")
st.image('images/ya.jpeg')

precios = pd.read_csv('precios.csv')
st.title("Gráfico")
st.header("En esta parte veras un hermoso grafico de barras que te especifica el porcentaje de los horarios nocturnos y diurno que hay en cada provincia")
fig,ax = plt.subplots()
# Crear el gráfico de barras
conteo_tipos = precios['provincia'].value_counts()
conteo_tipos.plot(kind='bar', ax=ax, color='skyblue')
# Agregar etiquetas y título
ax.set_xlabel('provincia')
ax.set_ylabel('Cantidad')
ax.set_title('Cantidad de provincia por tipohorario ')

# Mostrar el gráfico
st.pyplot(fig)
