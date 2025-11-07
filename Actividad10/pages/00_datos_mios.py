import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("información de los datos de esta pagina")
st.header("La información que obtienen en este archivo algunos precios de naftas ,horario de atencion nocturno y de dia como tambien los tipos de gasolina")
st.image('images/ya.jpeg')

precios = pd.read_csv('precios.csv')
st.title("los horarios que hay en cada provincia")
st.header("En esta parte veras un hermoso grafico de barras que te explica el porcentaje de los horarios nocturnos y diurno hay en casa provincia")
st.title("Gráfico")
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
