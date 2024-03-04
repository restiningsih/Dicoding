import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
dataset_path = "C:/Users/ASUS/Downloads/Bike-sharing-dataset/sewa_sepeda.csv"
sewa_sepeda = pd.read_csv(dataset_path)

# Sidebar
st.sidebar.title("Menu")
menu_selection = st.sidebar.radio("Pilih Menu", ["Tampilkan Dataset", "Tampilkan Box Chart dan Line Chart"])

# Main content
st.title("Aplikasi Analisis Sewa Sepeda")

if menu_selection == "Tampilkan Dataset":
    st.subheader("Dataset Sepeda")
    st.write(sewa_sepeda)

elif menu_selection == "Tampilkan Box Chart dan Line Chart":
    st.subheader("Box Chart")

    # Group by season and sum the total count
    total_sewa_per_season = sewa_sepeda.groupby('season_x')['cnt_y'].sum().reset_index()
    total_sewa_per_season.columns = ['Musim', 'Total Sewa Sepeda']

    # Create bar plot
    plt.bar(total_sewa_per_season['Musim'], total_sewa_per_season['Total Sewa Sepeda'], color='skyblue')
    plt.xlabel('Musim')
    plt.ylabel('Total Sewa Sepeda')
    plt.title('Box Chart: Total Sewa Sepeda per Musim')
    st.pyplot(plt)

    st.subheader("Line Chart")

    # Group by month and sum the total count
    jumlah_sewa = sewa_sepeda.groupby('mnth_x')['cnt_y'].sum().reset_index()
    jumlah_sewa.columns = ['Bulan', 'Total Sewa Sepeda']

    # Create line chart
    plt.plot(jumlah_sewa['Bulan'], jumlah_sewa['Total Sewa Sepeda'], marker='o', color='green')
    plt.xlabel('Bulan')
    plt.ylabel('Total Sewa Sepeda')
    plt.title('Line Chart: Total Sewa Sepeda per Bulan')
    st.pyplot(plt)
