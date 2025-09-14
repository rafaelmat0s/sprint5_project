import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles.csv')

st.header("Análise de Veículos")

hist_button = st.button("Criar Histograma")

if hist_button:
    st.write("Histograma do odômetro dos veículos")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button("Criar Gráfico de Dispersão")

if scatter_button:
    st.write("Gráfico de Dispersão - Preço vs Odômetro")
    fig = px.scatter(car_data, x="odometer", y="price", title="Preço vs Odômetro")
    st.plotly_chart(fig, use_container_width=True)

