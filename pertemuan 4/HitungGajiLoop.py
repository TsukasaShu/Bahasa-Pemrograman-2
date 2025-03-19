status = ["Tetap", "Honor"]
golongan = ["A", "B", "C"]

gaji = [1000000, 750000]

bonus_tetap = [200000, 400000, 550000]
bonus_honor = [150000, 275000, 480000]

for s in status:
    print(f"Status: {s}")
    for i in range(len(golongan)):
        if s == "Tetap":
            gaji_pokok = gaji[0]  
            bonus = bonus_tetap[i]
        else:
            gaji_pokok = gaji[1]  
            bonus = bonus_honor[i]
        
        total_gaji = gaji_pokok + bonus
        
        print(f"  Golongan: {golongan[i]}")
        print(f"  Gaji Pokok: Rp{gaji_pokok:,}")
        print(f"  Bonus: Rp{bonus:,}")
        print(f"  Total Gaji: Rp{total_gaji:,}\n")
