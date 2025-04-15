#Matriks 1
matriks_1 = [
    [1, 4, 7, 2, 5],
    [4, 2, 7, 3, 1],
    [9, 5, 3, 1, 3],
    [6, 8, 2, 3, 2],
    [3, 1, 6, 7, 7]
]

#Matriks 2
matriks_2 = [
    [2, 4, 7, 2, 5],
    [3, 8, 3, 5, 1],
    [8, 2, 4, 5, 2],
    [1, 9, 2, 8, 5],
    [4, 6, 1, 2, 7]
]

#Perkalian Matriks
hasil_matriks = []
for i in range(len(matriks_1)):
    row = []
    for j in range(len(matriks_2[0])):
        sum = 0
        for k in range(len(matriks_2)):
            sum += matriks_1[i][k] * matriks_2[k][j] 
        row.append(sum)
    hasil_matriks.append(row)


#Hasil perkalian matriks
print("Hasil Dari Perkalian Matriks : ")
for row in hasil_matriks:
    print(row)