def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)
        player = players[turn % 2]
        print(f"Player {player}'s turn")

#input move
        while True:
            try:
                row, col = map(int, input("Enter row and column (0-2): ").split())
                if board[row][col] == " ":
                    board[row][col] = player
                    break
                else:
                    print("Cell already taken. Choose another.")
            except (ValueError, IndexError):
                print("Invalid input. Enter two numbers between 0 and 2.")

        # Check win or draw
        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        turn += 1
# Run the game
if __name__ == "__main__":
    tic_tac_toe()

