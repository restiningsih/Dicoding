import streamlit as st
import pandas as pd
import seaborn as sns

# Load data
GitD = 'https://github.com/restiningsih/Dicoding/raw/main/day.csv'
GitH = 'https://github.com/restiningsih/Dicoding/raw/main/hour.csv'

hari = pd.read_csv(GitD)
jam = pd.read_csv(GitH)

st.sidebar.title('Proyek Streamlit :turkey: ')
menu_utama = st.sidebar.radio('Menu Navigasi:', ('Dataset Hari :calendar: ', 'Dataset Jam :clock1: ', 'Dataset Gabungan :dna: ', 'Visualisasi Data :bar_chart:'))

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
    
elif menu_utama =='Dataset Gabungan :dna: ':
    st.subheader('Dataset Gabungan')
    sewa_sepeda = pd.merge(
        left=hari,
        right=jam,
        how="left",
        left_on="season",
        right_on="hr"
    )
    st.dataframe(sewa_sepeda)
    
    data_min_max3 = {
        'Fitur': sewa_sepeda.columns,
        'Nilai Minimum': sewa_sepeda.min(),
        'Nilai Maksimum': sewa_sepeda.max()
    }
    df_min_max3 = pd.DataFrame(data_min_max3)

    st.write('Nilai Minimum dan Maksimum:')
    st.dataframe(df_min_max3)
    

elif menu_utama == 'Visualisasi Data :bar_chart:':
    st.subheader('Visualisasi Data')
    
    # Pastikan variabel sewa_sepeda dapat diakses di blok ini
    sewa_sepeda = pd.merge(
        left=hari,
        right=jam,
        how="left",
        left_on="season",
        right_on="hr"
    )
    
st.write("Bar Chart")
sns.barplot(x='season_x', y='cnt_y', data=sewa_sepeda)
st.pyplot()  # Menyertakan gambar yang dihasilkan oleh sns.barplot()

st.write('Gambar di atas merupakan gambar bar plot yang menampilkan tingkat sewa sepeda setiap musimnya. Musim 1 adalah musim yang paling banyak orang menggunakan jasa sewa sepeda')

st.write("Line Chart")
jumlah_sewa = sewa_sepeda.groupby('mnth_x')['cnt_y'].sum()
jumlah_sewa.plot(kind='line')
st.pyplot()  # Menyertakan gambar yang dihasilkan oleh jumlah_sewa.plot()

 st.write('Gambar di atas merupakan line chart yang menampilkan kondisi bisnis sewa sepeda setiap bulannya. Dapat dilihat bahwa kondisinya cenderung menurun, dan titik terendahnya berada di bulan 11.')
