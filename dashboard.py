import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='white')

# Import Dataset
df = pd.read_csv("day.csv")

# Konversi kolom 'dteday' ke tipe data datetime
df['dteday'] = pd.to_datetime(df['dteday'])

#Memberikan Judul Dashboard
st.title('Dashboard Bike Sharing Dataset')
 
#Membuat tab
tab1, tab2, tab3 = st.tabs(["Total Sewa", "Pola Data", "Analisis Lanjutan"])

with tab1:
    #Memberikan total sewa
    total = df.cnt.sum()
    st.metric("Total sewa", value=total)

    #Memberikan sub-header
    st.subheader('Jumlah penyewaan sepeda berdasarkan musim')

    #Memberikan bar-chart
    season = ('fall','summer','winter', 'springer')
    total = (1061129, 918589, 841613, 471348)
    fig, ax = plt.subplots()
    ax.bar(season, total, color=['#023e8a', '#00b4d8', '#00b4d8', '#00b4d8'])
    ax.set_xlabel('Musim')
    ax.set_ylabel('Total Penjualan')
    st.pyplot(fig)

    st.caption('Copyright (c) Rizki Ramadhani 2024')

with tab2:
    #Memberikan sub-header
    st.subheader('Pola data total penyewaan sepeda')

    #Memberikan line-chart
    daily_counts = df.groupby(by=df['dteday']).agg({'cnt': 'sum'})
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(daily_counts.index, daily_counts['cnt'], marker='o', linestyle='-')
    ax.set_xlabel('Date')
    ax.set_ylabel('Total Counts')
    ax.grid(True)
    st.pyplot(fig)

    st.caption('Copyright (c) Rizki Ramadhani 2024')  

with tab3:
    #Memberikan sub-header
    st.subheader('Korelasi Spearman')

    fig, ax = plt.subplots(figsize=(30,30))

    corr = df[['temp',
            'hum', 
            'windspeed', 
            'cnt']].corr(method='spearman')

    sns.heatmap(data=corr,
                    annot=True,
                    annot_kws={'size': 40})
    ax.tick_params(axis='x', labelsize=40)
    ax.tick_params(axis='y', labelsize=40)
    st.pyplot(fig)

    st.caption('Copyright (c) Rizki Ramadhani 2024')