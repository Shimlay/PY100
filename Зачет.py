def init_board(board_size):
    board = []
    for i in range(board_size):
        row = []
        for j in range(board_size):
            row.append(' ')
        board.append(row)
    return board


def draw_board(board):
    board_size = len(board)
    print(' ', end='')
    for i in range(board_size):
        print('  ', i, end='')
    print()
    print('  -' + '-'.join(['---' for i in range(board_size)]) + '-')
    for i in range(board_size):
        print(i, '|', end='')
        for j in range(board_size):
            print(' ' + board[i][j] + ' |', end='')
        print()
        print('  -' + '-'.join(['---' for i in range(board_size)]) + '-')


def check_win(board):
    board_size = len(board)
    for i in range(board_size):
        if board[i][0] != ' ' and all(board[i][j] == board[i][0] for j in range(1, board_size)):
            return True, board[i][0]
        if board[0][i] != ' ' and all(board[j][i] == board[0][i] for j in range(1, board_size)):
            return True, board[0][i]
    if board[0][0] != ' ' and all(board[i][i] == board[0][0] for i in range(1, board_size)):
        return True, board[0][0]
    if board[0][board_size - 1] != ' ' and all(
            board[i][board_size - i - 1] == board[0][board_size - 1] for i in range(1, board_size)):
        return True, board[0][board_size - 1]
    return False, ' '


def change_player(current_player, player_1, player_2):
    if current_player == player_1:
        return player_2
    else:
        return player_1


def play_game():
    board_size = int(input('Введите размер поля: '))
    player_1 = input('Введите имя игрока 1: ')
    player_2 = input('Введите имя игрока 2: ')
    board = init_board(board_size)
    current_player = player_1
    while True:
        draw_board(board)
        print('Ходит', current_player)
        row, col = map(int, input('Введите номер строки и столбца (через пробел): ').split())
        if row < 0 or row >= board_size or col < 0 or col >= board_size:
            print('Неверные координаты')
            continue
        if board[row][col] != ' ':
            print('Эта ячейка уже занята')
            continue
        board[row][col] = 'X' if current_player == player_1 else 'O'
        is_win, winner = check_win(board)
        if is_win:
            draw_board(board)
            print('Выиграл,', current_player)
            break
        current_player = change_player(current_player, player_1, player_2)


play_game()
