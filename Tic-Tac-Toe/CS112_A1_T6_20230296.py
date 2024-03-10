# Program: Tic-Tac-Toe with numbers. A board of 3 x 3 is displayed and player 1 takes odd numbers 1,
# 3, 5, 7, 9 and player 2 takes even numbers 0, 2, 4, 6, 8. Players take turns to write their
# numbers. Odd numbers start. Use each number only once. The first person to complete a line
# that adds up to 15 is the winner. The line can have both odd and even numbers
# Author: Kirolos Michel Helmy | ID: 20230296
# Version: 2.0
#Date: 03/02/2024
# ==================================================================================================

# Initial setup with player lists and an empty game board
player_1_list = [1, 3, 5, 7, 9]
player_2_list = [0, 2, 4, 6, 8]

board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
         
# Function to print the current state of the game board
def print_board(board):
    for row in board:
        for i in range(3):
            print("|",row[i], end=" | ")
        print()
        print('-' * 17)

# Display game instructions and player lists
print("Welcom to Tic-Tac-Toe Game")
print("One player uses the odd number between 1 to 9 and the other player uses the even numbers between 2 to 8.")
print("The odd number player goes first. The winner is the player who completes a row of three numbers that add up to 15")
print(f"player 1 list of numbers :{player_1_list} \nplayer 2 list of numbers:{player_2_list}")

# Game loop continues until both player lists are empty
while not (len(player_1_list) == len(player_2_list) == 0):
    # Player 1 turn
    # Take player 1 play as an input and validate it's an integer number and in its list
    while True:
        choice_1 = input("please choose an integer number from your list (player 1 list):")
        try:
            if int(choice_1) not in player_1_list:
                continue
            if isinstance(int(choice_1), int):
                break
        except ValueError:
            continue
    # take player 1 move by taking row and column number and validate it's an integer number between 1 and 3
    while True:
        row_1 = input('Enter row number [1 or 2 or 3] you want to put your number in : ')
        try:
            if int(row_1) not in [1,2,3] :
                continue
            if isinstance(int(row_1), int):
                break
        except ValueError:
            continue

    while True:
        column_1 = input('Enter column number [1 or 2 or 3] you want to put your number in: ')
        try:
            if int(column_1) not in [1, 2, 3] :
                continue
            if isinstance(int(column_1), int):
                break
        except ValueError:
            continue
    player_1_list.remove(int(choice_1))

# Make the move if the chosen position is unoccupied, otherwise ask for another move
    while True:
        if board[int(row_1) - 1][int(column_1) - 1] == 0:
            board[int(row_1) - 1][int(column_1) - 1] = int(choice_1)
            break
        else:
            print("this place is already occupied please choose another one.")
            while True:
                row_1 = input('Enter row number [1 or 2 or 3] you want to put your number in : ')
                try:
                    if int(row_1) not in [1, 2, 3]:
                        continue
                    if isinstance(int(row_1), int):
                        break
                except ValueError:
                    continue

            while True:
                column_1 = input('Enter column number [1 or 2 or 3] you want to put your number in: ')
                try:
                    if int(column_1) not in [1, 2, 3]:
                        continue
                    if isinstance(int(column_1), int):
                        break
                except ValueError:
                    continue
    # update game state
    print_board(board)
    print(f"player 1 list :{player_1_list}")
    print(f"player 2 list :{player_2_list}")
    
    # Check for a win condition for Player 1
    for row in board:
        if sum(row) == 15:
            print(f'player 1 wins!!')
            exit()

    for i in range(3):
        if board[0][i] + board[1][i] + board[2][i] == 15:
            print(f'player 1 wins!!')
            exit()

    if board[0][0] + board[1][1] + board[2][2] == 15 or board[0][2] + board[1][1] + board[2][0] == 15:
        print(f'player 1 wins!!')
        exit()

    # Player 2 turn
    # Take player 2 play as an input and validate it's an integer number and in its list
    while True:
        choice_2 = input("please choose an integer number from your list (player 2 list):")
        try:
            if int(choice_2) not in player_2_list:
                continue
            if isinstance(int(choice_2), int):
                break
        except ValueError:
            continue
    
    # take player 2 move by taking row and column number and validate it's an integer number between 1 and 3
    while True:
        row_2 = input('Enter row number [1 or 2 or 3] you want to put your number in : ')
        try:
            if int(row_2) not in [1, 2, 3]:
                continue
            if isinstance(int(row_2), int):
                break
        except ValueError:
            continue

    while True:
        column_2 = input('Enter column number [1 or 2 or 3] you want to put your number in: ')
        try:
            if int(column_2) not in [1, 2, 3]:
                continue
            if isinstance(int(column_2), int):
                break
        except ValueError:
            continue
    player_2_list.remove(int(choice_2))

    # Make the move if the chosen position is unoccupied, otherwise ask for another move
    while True:
        if board[int(row_2) - 1][int(column_2) - 1] == 0:
            board[int(row_2) - 1][int(column_2) - 1] = int(choice_2)
            break
        else:
            print("this place is already occupied please choose another one.")
            while True:
                row_2 = input('Enter row number [1 or 2 or 3] you want to put your number in : ')
                try:
                    if int(row_2) not in [1, 2, 3]:
                        continue
                    if isinstance(int(row_2), int):
                        break
                except ValueError:
                    continue

            while True:
                column_2 = input('Enter column number [1 or 2 or 3] you want to put your number in: ')
                try:
                    if int(column_2) not in [1, 2, 3]:
                        continue
                    if isinstance(int(column_2), int):
                        break
                except ValueError:
                    continue

    # update game state
    print_board(board)
    print(f"player 1 list :{player_1_list}")
    print(f"player 2 list :{player_2_list}")
    
    # Check for a win condition for Player 2
    for row in board:
        if sum(row) == 15:
            print(f'player 2 wins!')
            exit()

    for i in range(3):
        if board[0][i] + board[1][i] + board[2][i] == 15:
            print(f'player 2 wins!!')
            exit()

    if board[0][0] + board[1][1] + board[2][2] == 15 or board[0][2] + board[1][1] + board[2][0] == 15:
        print(f'player 2 wins!!!')
        exit()

print("the game is a draw!")
