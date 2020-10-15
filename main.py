import random
from is_win_checker import is_win

matrix = [
    ['', '', ''],
    ['', '', ''],
    ['', '', ''],
]

print(matrix)


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
    while is_win(matrix):
        player_step()
        print('win') if is_win(matrix) else print('play')
        print(matrix)
        comp_step()
        print(matrix)


game()