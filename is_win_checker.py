def is_win(matrix):
    row, col = 0, 0
    while row < 3:
        if matrix[row][col] == matrix[row][col + 1] == matrix[row][col + 2] != "":
            return True
        row += 1
    row, col = 0, 0
    while col < 3:
        if matrix[row][col] == matrix[row + 1][col] == matrix[row + 2][col] != "":
            return True
        col += 1
    row, col = 0, 0
    if matrix[row][col] == matrix[row + 1][col + 1] == matrix[row + 2][col + 2] != "":
        return True
    row, col = 0, 0
    if matrix[row][col + 2] == matrix[row + 1][col + 1] == matrix[row + 2][col] != "":
        return True
    return False
