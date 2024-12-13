import pandas as pd
import streamlit as st
import plotly.express as px
from scipy import stats
import matplotlib.pyplot as plt

df_vehicles = pd.read_csv('vehicles_us.csv')

Q1 = df_vehicles['price'].quantile(0.25)
Q3 = df_vehicles['price'].quantile(0.75)
IQR = Q3 - Q1

upper_bound = Q3 + 1.5 * IQR
lower_bound = Q1 - 1.5 * IQR

outliers = (df_vehicles['price'] < lower_bound) | (df_vehicles['price'] > upper_bound)

df_vehicles_no_outliers = df_vehicles[~outliers]

st.header("My Streamlit App")

show_histogram = st.checkbox("Show Histogram")

if show_histogram:
    fig = px.histogram(df_vehicles, x="price", title="Vehicles")
    st.plotly_chart(fig)
fig_hist_mpg = px.histogram(df_vehicles, x='odometer', title='Distribution of Odometer')
st.plotly_chart(fig_hist_mpg)

fig_hist_hp = px.histogram(df_vehicles, x='price', title='Distribution of Price')
st.plotly_chart(fig_hist_hp)


fig_scatter = px.scatter(df_vehicles, x='odometer', y='price', title='Odometer vs Price')
st.plotly_chart(fig_scatter)

fig = px.scatter(df_vehicles, x="odometer", y="price", title="Vehicles")
st.plotly_chart(fig)