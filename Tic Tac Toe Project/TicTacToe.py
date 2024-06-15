import random

def display_board(board):
    print('\n' * 10)
    print("    " + board[7] + "|" + board[8] + "|" + board[9])
    print("--------------")
    print("    " + board[4] + "|" + board[5] + "|" + board[6])
    print("---------------")
    print("    " + board[1] + "|" + board[2] + "|" + board[3])

def player_input():
    accepted_letters = ["X","O"]
    letter = "A"
    while letter not in accepted_letters:
        letter = input("What letter do you want as your marker? ")

    if letter == 'X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    if (mark == board[7] and mark == board[8] and mark == board[9]) or (mark == board[4] and mark == board[5] and mark == board[6]) or (mark == board[1] and mark == board[2] and mark == board[3]):
        return True
    elif (mark == board[7] and mark == board[4] and mark == board[1]) or (mark == board[8] and mark == board[5] and mark == board[2]) or (mark == board[9] and mark == board[6] and mark == board[3]):
        return True
    elif (mark == board[1] and mark == board[5] and mark == board[9]) or (mark == board[7] and mark == board[5] and mark == board[3]):
        return True
    return False

def choose_first():
    random_number = random.randint(1,2)
    if random_number == 1:
        return "Player 1"
    else:
        return "Player 2"

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input("Choose a position (1-9): "))

    return position

def replay():
    result = input("Do you want to play again? ('Y' for Yes, 'N' for No")
    if result == "Y":
        return True
    else:
        return False

print("Welcome to Tic Tac Toe!")

while True:

    the_board = [" "] * 10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(f"{turn} will go first.")

    play_game = input('Are you ready to play? Enter Y or N.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn == "Player 1":

            display_board(the_board)

            position = player_choice(the_board)

            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("Player 1 has WONNN!!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME")
                    game_on = False
                else:
                    turn = "Player 2"

        else:

            display_board(the_board)

            position = player_choice(the_board)

            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print("Player 2 has WONNN!!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME")
                    game_on = False
                else:
                    turn = "Player 1"

    if not replay():
        break
