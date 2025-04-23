# Function to place Queens on an n x n chessboard so that no two Queens attack each other
def Queen_placing(n):
    # Create an empty board with "." representing empty cells
    Board = [["."] * n for _ in range(n)]
    Solutions = []  # List to store all valid board arrangements

    # Function to check if it's safe to place a Queen at (row, colm)
    def is_safe(Board, row, colm, n):
        # Check the same column in all previous rows
        for i in range(row):
            if Board[i][colm] == "Q":
                return False

        # Check upper-left diagonal
        i, j = row - 1, colm - 1
        while i >= 0 and j >= 0:
            if Board[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        # Check upper-right diagonal
        i, j = row - 1, colm + 1
        while i >= 0 and j < n:
            if Board[i][j] == "Q":
                return False
            i -= 1
            j += 1

        return True  # It's safe to place the Queen

    # Recursive function to try placing Queens row by row
    def solve(row):
        # If all rows are filled, we found a valid solution
        if row == n:
            pattern = [" ".join(_) for _ in Board]  # Convert board rows to strings
            Solutions.append(pattern)  # Add the solution to the list
            return

        # Try placing a Queen in each column of the current row
        for colm in range(n):
            if is_safe(Board, row, colm, n):
                Board[row][colm] = "Q"  # Place the Queen
                solve(row + 1)  # Recur to place Queen in the next row
                Board[row][colm] = "."  # Backtrack and remove the Queen

    solve(0)  # Start solving from the first row
    return Solutions  # Return all valid solutions

# Print the solutions for a 4x4 board
result = Queen_placing(8)      # suppose this returns a list of solutions
for index, value in enumerate(result):
    print(f"Solution #{index}")
    for values in value:
        print(values) 
