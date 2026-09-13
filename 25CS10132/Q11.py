import numpy as np

def compute_matrix_properties(matrix):
    A = np.array(matrix)
    det = np.linalg.det(A)
    inv = np.linalg.inv(A)
    rank = np.linalg.matrix_rank(A)
    return det, inv, rank

if __name__ == "__main__":
    A = [[4, 3], 
         [3, 2]]

    determinant, inverse, rank = compute_matrix_properties(A)

    print("Matrix:")
    print(A)
    print("\nDeterminant:")
    print(determinant)
    print("\nInverse:")
    print(inverse)
    print("\nRank:")
    print(rank)