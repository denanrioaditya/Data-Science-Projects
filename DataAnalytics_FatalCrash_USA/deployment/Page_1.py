import streamlit as st
import pandas as pd
import numpy as np

def app():
    st.title ('Data Visualization')
    st.write ('This is Page For Data Visualization Dashboard')

    data = pd.read_csv('h8dsft_P0ML1_adnan_rio.csv')
    
    st.header ('Negara bagian jumlah kecelakaan paling tinggi')
    st.image ('plot.png')

    st.header ('Perbandingan antara Urban dan Rural')
    st.image ('plot1.png')

    st.header ('Frekeunsi jam kecelakaan paling tinggi')
    st.image ('plot2.png')

    st.header ('Frekuensi tipe mobil kecelakaan paling tinggi')
    st.image ('plot3.png')
    


