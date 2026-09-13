import numpy as np

def numpy_matrix_operations(A, B, C):
    A_np = np.array(A)
    B_np = np.array(B)
    C_np = np.array(C)
    
    addition = A_np + B_np
    subtraction = A_np - B_np
    multiplication = np.dot(A_np, C_np)
    transpose = A_np.T
    
    return addition, subtraction, multiplication, transpose

if __name__ == "__main__":
    print("--- WITH NUMPY ---")
    A = [[1, 2, 3], 
         [4, 5, 6]]
         
    B = [[7, 8, 9], 
         [1, 2, 3]]
         
    C = [[1, 2], 
         [3, 4], 
         [5, 6]]

    add, sub, mult, trans = numpy_matrix_operations(A, B, C)

    print("Matrix Addition (A + B):\n", add)
    print("\nMatrix Subtraction (A - B):\n", sub)
    print("\nMatrix Multiplication (A * C):\n", mult)
    print("\nMatrix Transpose (A^T):\n", trans)