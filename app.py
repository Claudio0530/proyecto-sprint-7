import pandas as pd
import plotly.express as px
import streamlit as st

# Título principal
st.header('Panel de Control: Análisis de Inventario de Vehículos')

# Leer los datos con un mensaje de carga
with st.spinner('Cargando base de datos...'):
    car_data = pd.read_csv('vehicles_us.csv')

st.success('¡Datos cargados correctamente!')

# Crear botones para los gráficos
hist_button = st.button('Generar Histograma de Kilometraje')

if hist_button:
    st.write('Distribución del kilometraje de los vehículos en venta')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Generar Gráfico de Dispersión (Precio vs Km)')

if scatter_button:
    st.write('Relación entre el precio y el kilometraje de los anuncios')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
