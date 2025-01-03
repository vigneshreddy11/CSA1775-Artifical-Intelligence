def print_solution(board):
    """Print the chessboard with queens placed."""
    for row in board:
        print(' '.join('Q' if cell == 1 else '.' for cell in row))
    print()

def is_safe(board, row, col):
    """Check if it's safe to place a queen at (row, col)."""
    # Check the column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check the upper-left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the upper-right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, len(board), 1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, row):
    """Solve the N-Queens problem using backtracking."""
    # If all queens are placed
    if row >= len(board):
        return True

    # Try placing a queen in each column of the current row
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1  # Place queen
            if solve_n_queens(board, row + 1):
                return True
            board[row][col] = 0  # Backtrack

    return False

def n_queens_solution(n):
    """Solve the N-Queens problem and print the board."""
    board = [[0 for _ in range(n)] for _ in range(n)]  # Initialize an empty board

    if solve_n_queens(board, 0):
        print_solution(board)
    else:
        print(f"No solution exists for {n}-Queens problem.")

# User input for board size (n)
n = int(input("Enter the size of the board (default is 8 for 8-Queens): ") or 8)

# Solve and print the solution
n_queens_solution(n)
