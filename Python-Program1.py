def multiply_matrices(matrix1, matrix2, r1, c1, r2, c2):
    result = [[0 for _ in range(c2)] for _ in range(r1)]
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result
def get_matrix_input(rows, cols):
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1} (space-separated values):").split()))
        matrix.append(row)
    return matrix
r1 = int(input("Enter the number of rows for Matrix 1: "))
c1 = int(input("Enter the number of columns for Matrix 1: "))
matrix1 = get_matrix_input(r1, c1)
r2 = int(input("Enter the number of rows for Matrix 2: "))
c2 = int(input("Enter the number of columns for Matrix 2: "))
matrix2 = get_matrix_input(r2, c2)
result = multiply_matrices(matrix1, matrix2, r1, c1, r2, c2)
if result:
    print("The product of the two matrices is:")
for row in result:
    print(row)
