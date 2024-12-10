import streamlit as st
import pandas as pd
import plotly.express as px

df_vehicles = pd.read_csv('vehicles_us.csv')

st.header("My Streamlit App")

show_histogram = st.checkbox("Show Histogram")

if show_histogram:
    fig = px.histogram(df_vehicles, x="price", title="Vehicles")
    st.plotly_chart(fig)

fig = px.scatter(df_vehicles, x="odometer", y="price", title="Vehicles")
st.plotly_chart(fig)