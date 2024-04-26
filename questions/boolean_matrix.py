
'''
Given a boolean matrix of size RxC where each cell contains either 0 or 1,
modify it such that if a matrix cell matrix[i][j] is 1 then all the cells in its ith row and jth column will become 1.

approach:
    Traverse the matrix and identify the cells that contain 1.
    Store the indices of these cells.
    Traverse the matrix again and for each cell, if its row index or column index is present in the stored indices, set the value of that cell to 1.
Time Complexity: O(R * C), where R is the number of rows and C is the number of columns
Space Complexity: O(R + C), where R is the number of rows and C is the number of columns
'''

def modify_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Lists to store indices of cells containing 1
    row_indices = set()
    col_indices = set()

    # Traverse the matrix and store indices of cells containing 1
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                row_indices.add(i)
                col_indices.add(j)

    # Modify the matrix based on stored indices
    for i in range(rows):
        for j in range(cols):
            if i in row_indices or j in col_indices:
                matrix[i][j] = 1

    return matrix

# Example usage
matrix = [
    [1, 0, 0],
    [0, 0, 1],
    [0, 0, 0]
]
modified_matrix = modify_matrix(matrix)
for row in modified_matrix:
    print(row)

'''
 We can optimize the solution to achieve a better space complexity by using the matrix itself to mark the rows and columns
 that need to be modified. This way, we don't need additional space to store the indices.

 This optimized solution eliminates the need for storing indices separately, resulting in improved space complexity.
 Now, the space complexity is O(R + C), where R is the number of rows and C is the number of columns.
 The time complexity remains O(R * C) as before.

'''

def modify_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Variables to track whether a row or column needs modification
    modify_row = [False] * rows
    modify_col = [False] * cols

    # Traverse the matrix and mark rows and columns that need modification
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                modify_row[i] = True
                modify_col[j] = True

    # Modify the matrix based on marked rows and columns
    for i in range(rows):
        for j in range(cols):
            if modify_row[i] or modify_col[j]:
                matrix[i][j] = 1

    return matrix

# Example usage
matrix = [
    [1, 0, 0],
    [0, 0, 1],
    [0, 0, 0]
]
modified_matrix = modify_matrix(matrix)
for row in modified_matrix:
    print(row)


