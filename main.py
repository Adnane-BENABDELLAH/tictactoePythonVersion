# ----------Global Variables---------

# Game Board (empty)
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

# if game is still going
game_still_going = True

# who won? tie?
winner = None

# whos turn is it?
current_player = "X"

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def play_game():
    # display initial board
    display_board()


    #while the game is still going
    while game_still_going:

        #handle a single turn
        hundle_turn(current_player)

        #check if the game has ended
        check_if_gameover()

        #flip to the other player
        flip_player()

    # The game has ended
    if winner == "X" or winner =="O":
        print(winner + " won!!")
    else:
        print("Tie!")

#handle a single turn of an arbitary player
def hundle_turn(current_player):
    print(current_player + "'s turn :")
    pos = input("choose a position from 1 to 9: ")
    while pos not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        pos = input("choose a position from 1 to 9: ")
    pos = int(pos) - 1
    while board[pos] != "-":
        pos = input("choose a position from 1 to 9: ")
        pos = int(pos) - 1
    board[pos] = current_player
    display_board()

def check_if_gameover():
    check_win()
    check_tie()

def check_win():
    #set up global variables
    global winner

    #check rows
    row_winner = check_rows()

    # check columns
    column_winner = check_columns()

    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

def check_rows():
    # set up global variables
    global game_still_going

    row1 = board[0] == board[1] == board[2] != "-"

    row2 = board[3] == board[4] == board[5] != "-"

    row3 = board[6] == board[7] == board[8] != "-"

    # return the winner X or O
    if row1:
        game_still_going = False
        # we need to return the player either X or O
        # we can check the player in the first row through board[0]
        return board[0]
    elif row2:
        game_still_going = False
        # we need to return the player either X or O
        # we can check the player in the second  row through board[3]
        return board[3]
    elif row3:
        game_still_going = False
        # we need to return the player either X or O
        # we can check the player in the third row through board[6]
        return board[6]

    return


def check_columns():
    # set up global variables
    global game_still_going

    col1 = board[0] == board[3] == board[6] != "-"

    col2 = board[1] == board[4] == board[7] != "-"

    col3 = board[2] == board[5] == board[8] != "-"

    # return the winner X or O
    if col1:
        game_still_going = False
        # we need to return the player either X or O
        # we can check the player in the first column through board[0]
        return board[0]
    elif col2:
        game_still_going = False
        # we need to return the player either X or O
        # we can check the player in the second column through board[1]
        return board[1]
    elif col3:
        game_still_going = False
        # we need to return the player either X or O
        # we can check the player in the third column through board[2]
        return board[2]
    return


def check_diagonals():
    # set up global variables
    global game_still_going
    diag1 = board[0] == board[4] == board[8] != "-"
    diag2 = board[2] == board[4] == board[6] != "-"

    if diag1:
        game_still_going = False
        return  board[0]
    elif diag2:
        game_still_going = False
        return  board[2]
    return

def check_tie():
    # set up global variables
    global game_still_going

    if "-" not in board:
        game_still_going = False
    return

def flip_player():
    # set up global variables
    global  current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


play_game()







# board
# display board
# play game
# handle turn
# check win
#     check row
#     check columns
#     check diagonals
# check tie
# flip player