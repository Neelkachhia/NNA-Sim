import numpy as np

MATRIX_SIZE = 8

print(f"--- Simulating the core operation for two {MATRIX_SIZE}x{MATRIX_SIZE} matrices ---")

matrix_a = np.random.randint(0, 10, size=(MATRIX_SIZE, MATRIX_SIZE))
matrix_b = np.random.randint(0, 10, size=(MATRIX_SIZE, MATRIX_SIZE))

print("\nMatrix A:\n", matrix_a)
print("\nMatrix B:\n", matrix_b)

result_matrix = np.matmul(matrix_a, matrix_b)

print("\nResult Matrix C:\n", result_matrix)
print("\n--- Core operation successful! ---")
