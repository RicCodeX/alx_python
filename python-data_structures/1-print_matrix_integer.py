def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print("Empty matrix")
        return

    for row in matrix:
        for i, num in enumerate(row):
            print("{:d}".format(num), end="")
            if i < len(row) - 1:
                print(" ", end="")
        print()  # Move to the next line after each row

# Example usage:
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print_matrix_integer(matrix)
    print("--")
    print_matrix_integer()
