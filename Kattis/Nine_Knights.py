import sys

board = []

for i in range(5):
    line = sys.stdin.readline().split()
    board.append(line[0])

count = 0
valid = True

for i in range(5):
    for j in range(5):
        if board[i][j] == 'k':
            count += 1
            if i - 2 >= 0:
                if j - 1 >= 0:
                    if board[i - 2][j - 1] == 'k':
                        valid = False
                        break
                if j + 1 < len(board[i]):
                    if board[i - 2][j + 1] == 'k':
                        valid = False
                        break
            if i + 2 < len(board):
                if j - 1 >= 0:
                    if board[i + 2][j - 1] == 'k':
                        valid = False
                        break
                if j + 1 < len(board[i]):
                    if board[i + 2][j + 1] == 'k':
                        valid = False
                        break
            if j - 2 >= 0:
                if i - 1 >= 0:
                    if board[i - 1][j - 2] == 'k':
                        valid = False
                        break
                if i + 1 < len(board[i]):
                    if board[i + 1][j - 2] == 'k':
                        valid = False
                        break
            if j + 2 < len(board):
                if i - 1 >= 0:
                    if board[i - 1][j + 2] == 'k':
                        valid = False
                        break
                if i + 1 < len(board[i]):
                    if board[i + 1][j + 2] == 'k':
                        valid = False
                        break

if count != 9:
    valid = False

if valid:
    print('valid')
else:
    print('invalid')
