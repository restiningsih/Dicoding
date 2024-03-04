import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data_path = "C:/Users/ASUS/Downloads/Bike-sharing-dataset/sewa_sepeda.csv"
sewa_sepeda = pd.read_csv(data_path)

# Sidebar menu
menu = st.sidebar.selectbox(
    'Menu',
    ('Tampilkan Dataset', 'Tampilkan Box Chart dan Line Chart')
)

# Main content based on sidebar menu selection
if menu == 'Tampilkan Dataset':
    st.subheader('Dataset Sepeda')
    st.write(sewa_sepeda)
elif menu == 'Tampilkan Box Chart dan Line Chart':
    st.subheader('Box Chart')
    # Plot box chart
    box_data = sewa_sepeda.groupby('season_x')['cnt_y'].sum()
    plt.bar(box_data.index, box_data.values)
    plt.xlabel('Musim')
    plt.ylabel('Total Sewa Sepeda')
    st.pyplot()

    st.subheader('Line Chart')
    # Plot line chart
    jumlah_sewa = sewa_sepeda.groupby('mnth_x')['cnt_y'].sum()
    plt.plot(jumlah_sewa.index, jumlah_sewa.values, marker='o', linestyle='-')
    plt.xlabel('Bulan')
    plt.ylabel('Total Sewa Sepeda')
    st.pyplot()
