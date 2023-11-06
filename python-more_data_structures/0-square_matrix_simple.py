def square_matrix_simple(matrix=[]):
    # Create a new matrix to store the squared values
    result_matrix = []
    for row in matrix:
        # Create a new row to store squared values for the current row
        squared_row = []

        # Iterate through each element in the current row
        for element in row:
            # Square the element and append to the squared_row
            squared_row.append(element ** 2)

        # Append the squared_row to the result_matrix
        result_matrix.append(squared_row)

    return result_matrix

# Test the function
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    new_matrix = square_matrix_simple(matrix)
    
    for row in new_matrix:
        print(row)
        
    for row in matrix:
        print(row)

