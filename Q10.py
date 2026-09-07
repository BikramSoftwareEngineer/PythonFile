def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()

def matrix_addition(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have the same dimensions for addition.")
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def matrix_subtraction(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have the same dimensions for subtraction.")
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def matrix_multiplication(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    if cols_A != rows_B:
        raise ValueError("Columns of Matrix A must match rows of Matrix B for multiplication.")
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result

def matrix_transpose(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

if __name__ == "__main__":
    print("--- WITHOUT NUMPY ---")
    A = [[1, 2, 3], 
         [4, 5, 6]]
         
    B = [[7, 8, 9], 
         [1, 2, 3]]
         
    C = [[1, 2], 
         [3, 4], 
         [5, 6]]

    print("Matrix Addition (A + B):")
    print_matrix(matrix_addition(A, B))

    print("Matrix Subtraction (A - B):")
    print_matrix(matrix_subtraction(A, B))

    print("Matrix Multiplication (A * C):")
    print_matrix(matrix_multiplication(A, C))

    print("Matrix Transpose (A^T):")
    print_matrix(matrix_transpose(A))