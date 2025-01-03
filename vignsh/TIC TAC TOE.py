

def initialize_board():
    """Initialize an empty 3x3 board."""
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    """Print the current game board."""
    print("\n")
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    """Check if the player has won."""
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Check row
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check column
            return True
    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:  # Check diagonal
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:  # Check anti-diagonal
        return True
    return False

def is_board_full(board):
    """Check if the board is full (no more moves can be made)."""
    return all([cell != ' ' for row in board for cell in row])

def player_move(board, player):
    """Handle player's move."""
    while True:
        try:
            row, col = input(f"Player {player}, enter your move (row and column from 0-2 separated by space): ").split()
            row, col = int(row), int(col)
            
            # Validate the move
            if row not in range(3) or col not in range(3):
                print("Invalid input! Please enter values between 0 and 2.")
                continue
            if board[row][col] != ' ':
                print("This position is already taken. Try again.")
                continue
            
            # Place the player's mark
            board[row][col] = player
            break
        except ValueError:
            print("Invalid input! Please enter two integers separated by space.")
        except IndexError:
            print("Invalid position! Please enter values between 0 and 2.")

def play_game():
    """Function to manage the game loop."""
    board = initialize_board()
    current_player = 'X'  # Player 'X' starts first
    
    while True:
        print_board(board)
        player_move(board, current_player)

        # Check if the current player won
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check if the board is full (tie)
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == '__main__':
    play_game()
