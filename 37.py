# Program 37
# Write a Python Program to Add Two Matrices

matrix_1 = [
    [8,4,6],
    [5,1,6],
    [1,4,3],
]
matrix_2 = [
    [3,4,5],
    [7,8,9],
    [7,1,4],
]
print("matrix 1 =")
for i in matrix_1:
        print(i)
print("matrix 2 =")
for j in matrix_2:
        print(j)
result = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
]

for i in range(len(matrix_1)):
        for j in range(len(matrix_2)):
                result[i][j] = matrix_1[i][j]+matrix_2[i][j]

print("Adition of both the marrices is : ")
for r in result:
        print(r)                