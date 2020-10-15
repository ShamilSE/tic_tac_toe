import random

matrix = [
    ['', '', ''],
    ['', '', ''],
    ['', '', ''],
]

print(matrix)


def is_win():
    row, col = 0, 0
    while row < 3:
        if matrix[row][col] == matrix[row][col + 1] == matrix[row][col + 2] != 0:
            return True
        row += 1
    row, col = 0, 0
    while col < 3:
        if matrix[row][col] == matrix[row + 1][col] == matrix[row + 2][col] != 0:
            return True
        col += 1
    row, col = 0, 0
    if matrix[row][col] == matrix[row + 1][col + 1] == matrix[row + 2][col + 2] != 0:
        return True
    row, col = 0, 0
    if matrix[row][col + 2] == matrix[row + 1][col + 1] == matrix[row + 2][col] != 0:
        return True
    return False


def gen_numbers():
    x, y = random.randrange(0, 3), random.randrange(0, 3)
    return [x, y]


def comp_step():
    [x, y] = gen_numbers()
    if matrix[x][y] == '':
        matrix[x][y] = 'o'
    else:
        comp_step()


def player_step():
    print('Enter the row number')
    x = int(input())
    print('Enter the column number')
    y = int(input())
    matrix[x][y] = 'x'


def game():
    while is_win():
        player_step()
        print(matrix)
        comp_step()
        print(matrix)


game()
