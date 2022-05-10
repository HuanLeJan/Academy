# Autor : Jan Nguyen

board = ['-', '-', '-', '-', '-', '-', '-', '-', '-'] # ['-'] * 9
currentplayer = None
winner = None
run = True
player1 = None
player2 = None


def player():
    global currentplayer, player1, player2
    if currentplayer == None:
        XO = ('X', 'O')
        player_inp = input('Player 1, please choose side - X or O : ')
        if player_inp == 'X' or player_inp == 'x':
            player1 = XO[0]
            player2 = XO[1]
            return player1, player2
        elif player_inp == 'O' or player_inp == 'o':
            player1 = XO[1]
            player2 = XO[0]
            return player1, player2
        else:
            error_1 = 'Wrong side, please enter X or O'
            return print(error_1), player()


def change_player(player1, player2):
    global currentplayer
    if currentplayer is None:
        currentplayer = player1
    elif currentplayer == player1:
        currentplayer = player2
    else:
        currentplayer = player1


def pole(board):
    print('')
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])


def move(board):
    global currentplayer
    Pole = int(input('{}: Choose field (from 1 to 9): '.format(currentplayer)))
    if Pole >= 1 and Pole <= 9 and board[Pole - 1] == '-':
        board[Pole - 1] = currentplayer

    else:
        print('Wrong field !'), move(board)



def check_win(board):
    global winner
    global run
    if board[0] == board[1] == board[2] != '-' or \
            board[3] == board[4] == board[5] != '-' or \
            board[6] == board[7] == board[8] != '-' or \
            board[0] == board[3] == board[6] != '-' or \
            board[1] == board[4] == board[7] != '-' or \
            board[2] == board[5] == board[8] != '-' or \
            board[2] == board[4] == board[6] != '-' or \
            board[0] == board[4] == board[8] != '-':
        winner = currentplayer
        result = 'Player {} Won !'.format(winner)
        run = False
        pole(board)
    elif '-' not in board and winner is None :
        result = 'TIE !'
        run = False
        pole(board)
    else :
        result = 'Next move !'
    return print(result), run

def main():
    while run is True:
        player()
        change_player(player1, player2)
        pole(board)
        move(board)
        check_win(board)


# main()
