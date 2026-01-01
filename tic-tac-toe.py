user_input = input("Do you want to play a game of Tic Tac Toe? (yes/no): ").strip().lower()
if user_input != 'yes':
    print("Maybe next time! Goodbye!")
    exit()
print("Great! Let's start the game of Tic Tac Toe!")
print("You will need to choose positions on a 3x3 grid to place your Xs and Os. If you get three in a row, you win! The positions are numbered from 1 to 9 as follows:")
print()
arr = [[None for _ in range(3)] for _ in range(3)]
k = 1
for i in range(3):
    for j in range(3):
        arr[i][j] = str(k)
        print(arr[i][j], end=" | " if j < 2 else "")
        k += 1
    print()
    if i < 2:
        print("---------")
print()

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None

def check_draw(board):
    for row in board:
        for cell in row:
            if cell not in ['X', 'O']:
                return False
    return True

def print_board(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ['X', 'O']:
                print(' ', end=" | " if j < 2 else "")
            else:
                print(board[i][j], end=" | " if j < 2 else "")
        print()
        if i < 2:
            print("---------")
    print()

def reset_board():
    new_board = [[None for _ in range(3)] for _ in range(3)]
    k = 1
    for i in range(3):
        for j in range(3):
            new_board[i][j] = str(k)
            k += 1
    return new_board

def play_again_prompt():
    response = input("Do you want to play again? (yes/no): ").strip().lower()
    return response == 'yes'

current_player = 'X'

while True:

    u_input = input("Enter the position (1-9) where you want to place your " + current_player + ": ").strip()

    if u_input not in [str(num) for num in range(1, 10)]:
        print("Invalid input. Please enter a number between 1 and 9.")
        continue

    pos = int(u_input) - 1
    row = pos // 3
    col = pos % 3

    if arr[row][col] in ['X', 'O']:
        print("Position already taken. Please choose another position.")
        continue

    arr[row][col] = current_player

    winner = check_winner(arr)
    if winner:
        print("Current board:\n")
        print()
        print_board(arr)
        print(f"Player {winner} wins! Congratulations!")

        if play_again_prompt():
            arr = reset_board()
            current_player = 'X'
            continue
        else:
            break

    if check_draw(arr):
        print("Current board:\n")
        print()
        print_board(arr)
        print("The game is a draw!")

        if play_again_prompt():
            arr = reset_board()
            current_player = 'X'
            continue
        else:
            break

    print("Current board:\n")
    print()
    print_board(arr)

    current_player = 'O' if current_player == 'X' else 'X'




