import random

# Membuat kamus sandi substitusi
alfabet = 'abcdefghijklmnopqrstuvwxyz'
sandikamus = {}
alfabetacak = list(alfabet)
random.shuffle(alfabetacak)
for i in range(len(alfabet)):
    sandikamus[alfabet[i]] = alfabetacak[i]

# Fungsi untuk mengenkripsi pesan
def enkripsi(pesan):
    pesan = pesan.lower()
    pesanenkripsi = ''
    for karakter in pesan:
        if karakter in sandikamus:
            pesanenkripsi += sandikamus[karakter]
        else:
            pesanenkripsi += karakter
    return pesanenkripsi

# Fungsi untuk mendekripsi pesan
def dekripsi(pesanenkripsi):
    pesandekripsi = ''
    for karakter in pesanenkripsi:
        for huruf, sandi in sandikamus.items():
            if karakter == sandi:
                pesandekripsi += huruf
                break
        else:
            pesandekripsi += karakter
    return pesandekripsi

# Pesan yang akan dienkripsi
pesan = "Aku Sayang Kamu "

# Proses enkripsi dan dekripsi
pesanenkripsi = enkripsi(pesan)
pesanterdekripsi = dekripsi(pesanenkripsi)

# Output hasil
print("Pesan Asli:", pesan)
print("Pesan Terenkripsi:", pesanenkripsi)
print("Pesan Terdekripsi:", pesanterdekripsi)
