import streamlit as st
import pandas as pd
import seaborn as sns

GitD = 'https://github.com/restiningsih/Dicoding/raw/main/day.csv'
GitH = 'https://github.com/restiningsih/Dicoding/raw/main/hour.csv'

hari = pd.read_csv(GitD)
jam = pd.read_csv(GitH)

st.sidebar.title('Proyek Streamlit :turkey: ')
menu_utama = st.sidebar.radio('Menu Navigasi:', ('Dataset Hari: ', 'Dataset Jam :clock1: ', 'Visualisasi Data :bar_chart:'))

if menu_utama =='Dataset Hari :calendar: ':
    st.subheader('Dataset sewa sepeda (dalam hari)')
    st.dataframe(hari)

    data_min_max1 = {
        'Fitur': hari.columns,
        'Nilai Minimum': hari.min(),
        'Nilai Maksimum': hari.max()
    }
    df_min_max1 = pd.DataFrame(data_min_max1)

    st.write('Nilai Minimum dan Maksimum:')
    st.dataframe(df_min_max1)

    st.write("Histogram Jumlah Pengunjung perbulannya")
    st.pyplot(hari['cnt'].hist())

elif menu_utama =='Dataset Jam :clock1: ':
    st.subheader('Dataset sewa sepeda (dalam jam)')
    st.dataframe(jam)
    
    data_min_max2 = {
        'Fitur': jam.columns,
        'Nilai Minimum': jam.min(),
        'Nilai Maksimum': jam.max()
    }
    df_min_max2 = pd.DataFrame(data_min_max2)

    st.write('Nilai Minimum dan Maksimum:')
    st.dataframe(df_min_max2)

    st.write("Histogram Jumlah Pengunjung perjamnya")
    st.pyplot(hari['cnt'].hist())
       
elif menu_utama == 'Visualisasi Data :bar_chart:':
    st.subheader('Visualisasi Data')
    
    st.write("Kondisi bisnis sepeda setiap musimnya")
    sns.barplot(x='season', y='cnt', data=hari)
    st.pyplot() 

    st.write('Gambar di atas merupakan gambar bar plot yang menampilkan tingkat sewa sepeda setiap musimnya. Musim 3 adalah musim yang paling banyak orang menggunakan jasa sewa sepeda')

    st.write("Kondisi bisnis sepeda setiap bulannya")
    sns.barplot(x='mnth', y='cnt', data=hari)
    st.pyplot()
    
    st.write('Kondisi bisnis sewa sepeda dapat terlihat naik hingga bulan ke-6. Selanjutnya malah makin rendah ketika mencapai penghujung tahun.')

    st.write("Kondisi bisnis sepeda setiap jamnya")
    sns.barplot(x='hr', y='cnt', data=jam)
    st.pyplot()

    st.write(" Kondisi bisnis sepeda cenderung ramai pada pukul 17 hingga 18 waktu setempat dan mencapai titik paling sepi di pukul 4 pagi.")
