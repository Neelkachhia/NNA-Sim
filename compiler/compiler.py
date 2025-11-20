def generate_instructions(matrix_size, array_size, output_file):
    print(f" \n--- COMPILER: Generating instructions for a {matrix_size}x{matrix_size} problem on a {array_size}x{array_size} array --- ")

    if matrix_size % array_size != 0:
        print("Error: Matrix size must be divisible by array size.")
        return

    # Calculate how many 4x4 tiles fit along one dimension
    tiles_per_dim = matrix_size // array_size

    with open(output_file, 'w') as f:
        # For each tile in the output matrix...
        for row_tile in range(tiles_per_dim):
            for col_tile in range(tiles_per_dim):
                # ... we need to perform this many inner multiplications
                for inner_tile in range(tiles_per_dim):
                    f.write(f"# Executing tile for output[{row_tile}][{col_tile}]\n")
                    f.write("LOAD\n")   # Load a tile of Matrix A
                    f.write("LOAD\n")   # Load a tile of Matrix B
                    f.write("EXECUTE\n") # Perform one 4x4 multiplication
                    f.write("STORE\n")  # Store the partial result

    print(f"--- COMPILER: Instructions written to {output_file} ---")

if __name__ == '__main__':
    # Generate instructions for an 8x8 problem on our 4x4 hardware
    generate_instructions(matrix_size=8, array_size=4, output_file='../instructions.txt')