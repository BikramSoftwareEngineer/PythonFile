import numpy as np

def compute_eigen(matrix):
    A = np.array(matrix)
    eigenvalues, eigenvectors = np.linalg.eig(A)
    return eigenvalues, eigenvectors

if __name__ == "__main__":
    A = [[4, -2], 
         [1,  1]]

    eigenvalues, eigenvectors = compute_eigen(A)

    print("Matrix:")
    print(A)
    print("\nEigenvalues:")
    print(eigenvalues)
    print("\nEigenvectors:")
    print(eigenvectors)