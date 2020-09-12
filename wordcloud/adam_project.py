# Program untuk generate kata-kata terbanyak ke wordcloud dengan excel

# import library yang dibutuhkan
from wordcloud import WordCloud, STOPWORDS # Untuk Generate WordCloud Menjadi Gambar (STOPWORDS Berfungsi untuk menampilkan salah satu kata agar tidak dobel)
import matplotlib.pyplot as plot # Untuk Menampilkan Hasil WordCloud
import pandas as panda # Untuk Memecah File Excel .csv

# Membaca File 'test.csv' yang telah dibuat tadi
file_csv = panda.read_csv(r"test.csv", encoding="latin-1")

content_kata = ''
katastop = set(STOPWORDS) # (STOPWORDS Berfungsi untuk menampilkan salah satu kata agar tidak dobel)

# iterate through the csv file 
for kata in file_csv.CONTENT: # test.csv kolom CONTENT

    # typecaste each val to string
    kata = str(kata)

    # split the value
    pecah_kata = kata.split() # Pecah Kata2 dulu

    # KOnversi hasil pecahan kata ke huruf kecil semua
    for i in range(len(pecah_kata)):
        pecah_kata[i] = pecah_kata[i].lower()

    content_kata += " ".join(pecah_kata) + " " # menggabungkan pecahan kata menjadi satu

# masukkan kata ke WordCloud
wordcloud = WordCloud(width=800, height=800,
                      background_color='white',
                      stopwords=katastop,
                      min_font_size=10).generate(content_kata)

# menampilkan hasil wordcloud dengan library plot
plot.figure(figsize=(8, 8), facecolor=None)
plot.imshow(wordcloud)
plot.axis("off")
plot.tight_layout(pad=0)

# tampilkan kata wordcloud yang sudah di plot
plot.show()
