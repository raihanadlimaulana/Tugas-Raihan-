import numpy as np

C = np.array([[4, 8],[9, 5],[6, 3]])
D = np.array([[4, 7, 9],[8, 6, 3]])

def matrix_multiplication(A, B):
    if A.shape[1] == B.shape[0]:
        return np.dot(A, B)

print("Matriks C:")
print(C)
print("\nMatriks D:")
print(D)

result_multiplication = matrix_multiplication(C, D)
print("\nHasil Perkalian Matriks c dan D:")
print(result_multiplication)

Matriks C:
[[4 8]
 [9 5]
 [6 3]]

Matriks D:
[[4 7 9]
 [8 6 3]]

Hasil Perkalian Matriks c dan D:
[[80 76 60]
 [76 93 96]
 [48 60 63]]
