import streamlit as st
import numpy as np

def app ():
    st.title ('Statistical Analysis')
    st.write ('This is Page For Statistical Analysis Dashboard')

    st.header ('Kasus')
    st.subheader ('Penjabaran')
    st.write ('''Departemen Pengawasan Lalu Lintas Kementerian Perhubungan Amerika Serikat ingin 
    mengetahui kondisi kasus kecelakaan yang terjadi di jalan selama tahun 2016 yang berguna untuk 
    diterapkan kebijakan baru supaya dapat mengurangi angka kecelakaan di kemudian hari.''')


    st.header ('Descriptive Statistics')
    st.subheader ('Penjabaran')
    st.write ('Analisa Central Tendency')
    st.image ('plot4.png')
    st.write ('KESIMPULAN : ')
    st.write ('''Dari sini kita bisa melihat mean, median, modus dari land_use_name urban''')


    st.header ('Inferential Statistics')
    st.subheader ('Penjabaran')
    st.write ('Hipotesis Testing')
    st.write ('Untuk Mengecek Apakah Kecelakan lebih banyak terjadi di land_use_name Urban atau Rural')
    st.write ('Hipotesis Kita Dalam Kasus Ini: ')
    st.write ('H0: μ_Urban == μ_Rural')
    st.write ('H1: μ_Urban != μ_Rural')
    st.write ('P-value: 0.876951438670603')
    st.write ('KESIMPULAN : ')
    st.write ('''Perhitungan menunjukan bahwa tidak terdapat perbedaan rata-rata kecelakaan diwilayah urban maupun rural yang signifikan,
    hal tersebut dapat menjadi pertimbangan pemerintah untuk memberlakukan kebijakan pembatasan kecepatan kendaraan di jam sibuk dan juga memberikan 
    rambu peringatan agar masyarakat lebih berhati-hati dimana kebijakan tersebut bersekala nasional''')