import random

def display_board(board):
    print('     |     |')
    print('  ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9])
    print('     |     |')
    print('-----------------')
    print('     |     |')
    print('  ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6])
    print('     |     |')
    print('-----------------')
    print('     |     |')
    print('  ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3])
    print('     |     |')

def player_input():
    marker = ''
    while marker not in ['X','O']:
        marker = input("Player 1, please pick a marker 'X' or 'O': ").upper()
    if marker == 'X':
        return 'X', 'O'
    elif marker == 'O':
        return 'O', 'X'


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return (board[7] == mark and board[8] == mark and board[9] == mark) or (board[4] == mark and board[5] == mark and board[6] == mark) or (board[1] == mark and board[2] == mark and board[3] == mark) or (board[1] == mark and board[4] == mark and board[7] == mark) or (board[2] == mark and board[5] == mark and board[8] == mark) or (board[3] == mark and board[6] == mark and board[9] == mark) or (board[7] == mark and board[5] == mark and board[3] == mark) or (board[1] == mark and board[5] == mark and board[9] == mark)


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):
    return board[position] == ' '

def board_full(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in range(1,10) or not space_check(board, position):
        position = input('Select a space: ')
        if position not in '123456789':
            print('Please select a number between 1 and 9')
            continue
        position = int(position)
        if not space_check(board,position):
            print('That space is already taken')
            continue
        return position


def replay():
    return input('Play again? y/n: ').lower().startswith('y')


print('Welcome to Tic-Tac-Toe')
while True:
    turn = choose_first()
    marker1, marker2 = player_input()
    print(f'By random selection, {turn} will start')
    theboard = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    play_game = input('Are you ready to play? Enter Yes or No.')
    if play_game.lower()[0] == 'y':
        game_on = True
        display_board(theboard)
    else:
        game_on = False
    while game_on:
        if turn == 'Player 1':
            print('Player 1:')
            choice = player_choice(theboard)
            place_marker(theboard, marker1, choice)
            display_board(theboard)
            if win_check(theboard, marker1):
                print("Player 1 wins! Congratulations")
                game_on = False
            else:
                if board_full(theboard):
                    print('Its a draw!')
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            print('Player 2:')
            choice = player_choice(theboard)
            place_marker(theboard, marker2, choice)
            display_board(theboard)
            if win_check(theboard, marker2):
                print("Player 2 wins! Congratulations")
                game_on = False
            else:
                if board_full(theboard):
                    print('Its a draw!')
                    game_on = False
                else:
                    turn = 'Player 1'
    if not replay():
        break