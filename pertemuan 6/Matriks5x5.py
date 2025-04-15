#Matriks 1
matrix_1 = [
    [1, 4, 7, 2, 5],
    [4, 2, 7, 3, 1],
    [9, 5, 3, 1, 3],
    [6, 8, 2, 3, 2],
    [3, 1, 6, 7, 7]
]

#Matriks 2
matrix_2 = [
    [2, 4, 7, 2, 5],
    [3, 8, 3, 5, 1],
    [8, 2, 4, 5, 2],
    [1, 9, 2, 8, 5],
    [4, 6, 1, 2, 7]
]

#Perkalian Matriks
result_matrix = []
for i in range(len(matrix_1)):
    row = []
    for j in range(len(matrix_2[0])):
        sum = 0
        for k in range(len(matrix_2)):
            sum += matrix_1[i][k] * matrix_2[k][j] 
        row.append(sum)
    result_matrix.append(row)


#Hasil perkalian matriks
print("Hasil Dari Perkalian Matriks : ")
for row in result_matrix:
    print(row)