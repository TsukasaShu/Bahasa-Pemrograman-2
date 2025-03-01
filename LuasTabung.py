import math

r = float(input("Masukkan Ukuran Jari-jari Lingkaran Tabung : "))
t = float(input("Masukkan Ukuran Tinggi Tabung : "))

volume = math.pi * math.pow(r, 2) * t

print("Volume Tabung Dengan Jari-jari Lingkaran", r, "Dan Dengan Tinggi", t, "Adalah :", volume)
