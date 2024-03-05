import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "C:/Users/ASUS/Downloads/Bike-sharing-dataset/sewa_sepeda.csv"
sewa_sepeda = pd.read_csv(file_path)

# Sidebar
st.sidebar.title("Menu Navigasi :turkey: ")
menu_selection = st.sidebar.radio("Pilih salah satu", ("Tampilkan dataset", "Tampilkan Bar Chart dan Line Chart"))

if menu_selection == "Tampilkan dataset":
    st.subheader("Dataset Bisnis Sewa Sepeda")
    st.write(sewa_sepeda)

    st.write("Dataset di atas merupakan dataset gabungan dari hour.csv dan day.csv. Kedua dataset tersebut membahas tentang bisnis sewa sepeda.")    
    
elif menu_selection == "Tampilkan Bar Chart dan Line Chart":
    
    st.subheader("Tingkat sewa sepeda setiap musimnya")
    box_data = sewa_sepeda.groupby('season_x')['cnt_y'].sum()
    fig_box = plt.figure()
    plt.bar(box_data.index, box_data.values)
    plt.xlabel('Musim')
    plt.ylabel('Total sewa sepeda')
    st.pyplot(fig_box)

    st.write("Gambar dia atas merupakan bar chart yang menampilkan banyaknya jumlah sewa sepeda dalam suatu musim. Musim 1 adalah musim yang paling tinggi permintaan sewa sepeda.")

    st.subheader("Tingkat sewa sepeda setiap bulannya")
    jumlah_sewa = sewa_sepeda.groupby('mnth_x')['cnt_y'].sum()
    fig_line = plt.figure()
    plt.plot(jumlah_sewa.index, jumlah_sewa.values, marker='o')
    plt.xlabel('Bulan')
    plt.ylabel('Total sewa sepeda')
    st.pyplot(fig_line)

    st.write("gambar di atas merupakan line chart yang menampilkan kondisi bisnis sewa sepeda yang dilakukan. Bisnis ini cenderung memiliki permintaan yang terus menurun setiap bulannya. Titik rendahnya adalah pada bulan ke 11.")
