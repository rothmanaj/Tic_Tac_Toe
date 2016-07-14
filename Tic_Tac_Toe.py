import os

def reset_board():
    return [[' ']*3,[' ']*3,[' ']*3]

def print_board(b):
    print ""
    print "%s | %s | %s" %(b[0][0], b[0][1], b[0][2])
    print "----------"
    print "%s | %s | %s" %(b[1][0], b[1][1], b[1][2])
    print "----------"
    print "%s | %s | %s" %(b[2][0], b[2][1], b[2][2])
    print ""

def check_status():

    global board, game_over

    game_over = "draw"

    for row in board:
        for place in row:
            if place == " ":
                game_over = ""

    for winner_test in ["X", "O"]:
        for i in range(0, 3):
            if board[i].count(winner_test) == 3:
                game_over = winner_test
        for col in range(0, 3):
            sum = 0
            for row in range(0, 3):
                if board[row][col] == winner_test:
                    sum += 1
            if sum == 3:
                game_over = winner_test
        if board[0][0] == winner_test and board[1][1] == winner_test and board[2][2] == winner_test:
            game_over = winner_test
        if board[0][2] == winner_test and board[1][1] == winner_test and board[2][0] == winner_test:
            game_over = winner_test

def get_computer_move():

    global board, turn

    empty_block = {"row": -1, "col": -1}
    max_move_block = {"row": -1, "col": -1}
    win_block = {"row": -1, "col": -1}
    stop_block = {"row": -1, "col": -1}

    for row in range(0, 3):
        for col in range(0, 3):
            if board[row][col] == " ":
                if max_move_block == empty_block:
                    max_move_block = {"row": row, "col": col}
                    max_move_score = 0

                # horizontal
                sh = 0
                tally = True
                win_chance = 0
                stop_chance = 0
                for c in range(0, 3):
                    if board[row][c] == " ":
                        if tally: sh += 1
                    elif board[row][c] == turn:
                        win_chance += 1
                    else:
                        stop_chance += 1
                        sh = 0
                        tally = False
                if win_chance == 2:
                    win_block = {"row": row, "col": col}
                if stop_chance == 2:
                    stop_block = {"row": row, "col": col}

                # vertical
                sv = 0
                tally = True
                win_chance = 0
                stop_chance = 0
                for r in range(0, 3):
                    if board[r][col] == " ":
                        if tally: sv += 1
                    elif board[r][col] == turn:
                        win_chance += 1
                    else:
                        stop_chance += 1
                        sh = 0
                        tally = False
                if win_chance == 2:
                    win_block = {"row": row, "col": col}
                if stop_chance == 2:
                    stop_block = {"row": row, "col": col}

                # diag_up
                sdu = 0
                tally = True
                win_chance = 0
                stop_chance = 0
                if (row == 0 and col == 0):
                    r = 0
                    c = 0
                elif (row == 1 and col == 0) or (row == 0 and col == 1):
                    r = 1
                    c = 0
                elif (row == 2 and col == 0) or (row == 1 and col == 1) or (row == 0 and col == 2):
                    r = 2
                    c = 0
                elif (row == 2 and col == 1) or (row == 1 and col == 2):
                    r = 2
                    c = 1
                elif (row == 2 and col == 2):
                    r = 2
                    c = 2
                while r >= 0 and c <= 2:
                    if board[r][c] == " ":
                        if tally: sdu += 1
                    elif board[r][c] == turn:
                        win_chance += 1
                    else:
                        stop_chance += 1
                        sdu = 0
                        tally = False
                    r -= 1
                    c += 1
                if win_chance == 2:
                    win_block = {"row": row, "col": col}
                if stop_chance == 2:
                    stop_block = {"row": row, "col": col}

                # diag_down
                sdd = 0
                tally = True
                win_chance = 0
                stop_chance = 0
                if (row == 0 and col == 2):
                    r = 0
                    c = 2
                elif (row == 0 and col == 1) or (row == 1 and col == 2):
                    r = 0
                    c = 1
                elif (row == 0 and col == 0) or (row == 1 and col == 1) or (row == 2 and col == 2):
                    r = 0
                    c = 0
                elif (row == 1 and col == 0) or (row == 2 and col == 1):
                    r = 1
                    c = 0
                elif (row == 2 and col == 0):
                    r = 2
                    c = 0
                while r <= 2 and c <= 2:
                    if board[r][c] == " ":
                        if tally: sdd += 1
                    elif board[r][c] == turn:
                        win_chance += 1
                    else:
                        stop_chance += 1
                        sdd = 0
                        tally = False
                    r += 1
                    c += 1
                if win_chance == 2:
                    win_block = {"row": row, "col": col}
                if stop_chance == 2:
                    stop_block = {"row": row, "col": col}

                if sh + sv + sdu + sdd > max_move_score:
                    max_move_score = sh + sv + sdu + sdd
                    max_move_block = {"row": row, "col": col}

    if win_block <> empty_block:
        return win_block
    elif stop_block <> empty_block:
        return stop_block
    else:
        return max_move_block


def make_move(row, col):

    global board, turn

    if board[row][col] == " ":
        board[row][col] = turn
        if turn == "X":
            turn = "O"
        elif turn == "O":
            turn = "X"


def get_move():

    global board, turn, player, game_over

    if turn <> player:
        move = get_computer_move()
        print "I go %s %s" % (move['row'], move['col'])
        make_move(move["row"], move["col"])
    elif turn == player:
        print "You are %s" % player
        print ""
        meet_requirements = False
        while not meet_requirements:
            turn_string = raw_input("To make a move type the row and columb for your move: ")
            move_comp = turn_string.split()
            x = int(move_comp[0])
            y = int(move_comp[1])
            if x >= 0 and x <= 2 and y >= 0 and y <= 2:
                if board[x][y] == " ":
                    meet_requirements = True
                else:
                    print ""
                    print "That is an invalid move. Try again..."
                    print ""
        make_move(int(move_comp[0]), int(move_comp[1]))

# Tick-Tack_Toe

stop = False

os.system('clear')
print "Welcome to TIC TAC TOE"

while stop == False:

    board = reset_board()
    game_over = ''  # set to 'draw' if draw, 'X' if X wins, 'O' if O wins

    print ""
    player = raw_input("Choose O's or X's: ")
    print ""
    print "You will be playing %s" % player
    print "X goes first"

    turn = 'X'

    if player == turn:
        print_board(board)

    while game_over == "":
        get_move()
        print_board(board)
        check_status()

    if game_over == "draw":
        print "A draw..."
    elif game_over == "X" or game_over == "O":
        if player == game_over:
            print "Yeeah - you win!!"
        else:
            print "Beat you again... Better luck next time."

    quit = raw_input("Do you want to play again? (Y/N): ")
    if quit == "N":
        stop = True

os.system('clear')
print ""
print "Goodbye till next time..."
print ""