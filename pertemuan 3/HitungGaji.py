def input_data():
    #Input Data Pegawai
    nama = input("Masukkan Nama Pegawai : ").title()
    nik = input("Masukkan Nomor NIK Pegawai : ")
    status = input("Masukkan Status Pegawai (Tetap/Honor) : ").strip().capitalize()
    golongan = input("Masukkan golongan pegawai (A/B/C) : ").strip().upper()

    #Inisialisasi gaji berdasarkan status dan golongan
    if status == "Tetap":
        Gaji = 1000000
        if golongan == "A":
            Bonus = 200000
        elif golongan == "B":
            Bonus = 400000
        elif golongan == "C":
            Bonus = 550000
        else:
            print("\nGolongan Tidak Valid \n")
            return False
    elif status == "Honor":
        Gaji = 750000
        if golongan == "A":
            Bonus = 150000
        elif golongan == "B":
            Bonus = 275000
        elif golongan == "C":
            Bonus = 480000
        else:
            print("\nGolongan Tidak Valid \n")
            return False
    else:
        print("\nStatus Tidak Valid  \n")
        return False


    #Hitung gaji total
    Gaji_Total = Gaji + Bonus

    #Print Hasil Gaji
    print("\n=====Laporan Gaji Pegawai=====\n")
    print("Nama Pegawai : ", nama)
    print("Nomor NIK Pegawai : ", nik)
    print("Status Pegawai : ", status)
    print("Golongan Pegawai : ", golongan)
    print("Gaji Pegawai :  Rp", Gaji)
    print("Bonus Pegawai :  Rp", Bonus)
    print("Total Gaji Pegawai :  Rp", Gaji_Total, "\n")
    return True

while True:
    if input_data():
        break