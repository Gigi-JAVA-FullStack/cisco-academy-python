import random
"""SUMMARY OF THE COMPONENTs FROM:
    print_board(board)
    is_winner(board, player)
    is_tie(board)
    is_valid_move(board, row, col)
    make_move(board, player, row, col)
    computer_move(board)
    player_move(board, player)
MAIN function: play_game()"""

def print_board(board):
    """Prints the board to the players moves."""
# Loop iterates through each row in the board list and prints
    for row in board:
# Prints each row of the board | join method - JOIN elements of the ROW list with the string "|" in between them.
        print(" | ".join(row))
# Repeat the dash character "-"" nine times for each row
        print("-" * 9)

def check_rows(board, player):
    """Function that checks if the player has won in any of the rows (horizontal lines).
-> looping through each row in the game board.
-> FOR each row, assuming initially that it's a match.
-> then going through the cells in that row, one by one.
-> If any cell in the row doesn't have the player's symbol (like X or O), the row is not a match.
-> If all cells in the row have the player's symbol, RETURN True (meaning the player has won in that row).
-> checked all rows and didn't find any row where the player has won
-> RETURN False (meaning the player hasn't won in any row)."""

# Loop through each row in the game board.
    for row in board:
# Check if all the cells in the current row have the player's symbol.
        row_match = True  # Assume the row is a match initially.
        for cell in row:
# Loop through each cell in the current row.
            if cell != player:
# If any cell in the row doesn't have the player's symbol, it's not a match.
                row_match = False  # Mark the row as not a match.
                break  # Exit the cell loop since we know the row is not a match.
        if row_match:
# If all cells in the current row have the player's symbol,
# then the player has won in this row.
            return True
# If we checked all rows and didn't find a row where the player has won, return False.
    return False

def check_columns(board, player):
    """Function that checks if the player has won in any of the columns (vertical lines).
-> looping through each column in the game board.
-> FOR each column, assume initially that it's a match (meaning the player has won in that column).
-> then going through the cells in that column, one by one.
-> If any cell in the column doesn't have the player's symbol (like X or O), we know the column is not a match.
-> If all cells in the column have the player's symbol, RETURN True (meaning the player has won in that column).
-> If checked all columns and didn't find any column where the player has won
-> RETURN False (meaning the player hasn't won in any column)."""

# Loop through each column in the game board.
    for col in range(3):
# Check if all the cells in the current column have the player's symbol.
        column_match = True  # Assume the column is a match at the beginning.
# Loop through each row in the current column.
        for row in range(3):
            if board[row][col] != player:
                # If any cell in the column doesn't have the player's symbol,
                # then the column is not a match.
                column_match = False  # Mark the column as not a match.
                break  # Exit the row loop since we know the column is not a match.
# If all cells in the current column have the player's symbol,
# then the player has won in this column.
        if column_match:
            return True
# If we checked all columns and didn't find a column where the player has won,
# return False to indicate the player hasn't won in any column.
    return False

def check_diagonals(board, player):
    """Function that checks if the player has won in either the main diagonal (top-left to bottom-right) or the anti-diagonal (top-right to bottom-left).
-> assume initially that both the main diagonal and the anti-diagonal are matches (meaning the player has won in those diagonals).
-> looping through the cells of the main diagonal (where the row index is the same as the column index).
-> If any cell in the main diagonal doesn't have the player's symbol, know the main diagonal is not a match.
-> looping through the cells of the anti-diagonal (where the row index stays the same, but the column index changes).
-> If any cell in the anti-diagonal doesn't have the player's symbol, know the anti-diagonal is not a match.
-> If either the main diagonal or the anti-diagonal is a match, we return True (meaning the player has won in one of the diagonals). Otherwise, we return False."""

# Check the main diagonal (from top-left to bottom-right)
    main_diag_match = True  # Assume the main diagonal is a match initially.
# Loop through the diagonal cells (same row and column index) of the main diagonal.
    for i in range(3):
        if board[i][i] != player:
# If any cell doesn't have the player's symbol, the main diagonal is not a match.
            main_diag_match = False  # Mark it as not a match.
            break  # Exit the loop since the diagonal is not a match.
# Check the anti-diagonal (from top-right to bottom-left)
    anti_diag_match = True  # Assume the anti-diagonal is a match initially.
# Loop through the cells of the anti-diagonal (row index stays the same, but column index changes).
    for i in range(3):
        if board[i][2 - i] != player:
# If any cell doesn't have the player's symbol, the anti-diagonal is not a match.
            anti_diag_match = False  # Mark it as not a match.
            break  # Exit the loop since the diagonal is not a match.
# Return True if either the main diagonal or anti-diagonal is a match, otherwise return False.
    return main_diag_match or anti_diag_match

def the_winner_is(board, player):
    """Function named the_winner_is that determines if a player has won the game.
-> Check if the player has won in rows, columns, or diagonals.
-> If the player has won in any direction (rows, columns, or diagonals), print "Yes, the player has won!" and return True.
-> If the player has not won in any direction, print "No, the player hasn't won yet." and return False."""

# Check if the player has won in rows, columns, or diagonals.
    if check_rows(board, player) or check_columns(board, player) or check_diagonals(board, player):
# If the player has won in any direction, return True.
        return True
    else:
# If the player has not won in any direction, return False.
        return False

def is_tie(board):
    """Check if the game is a tie"""
# meaning that all cells on the board are filled with either "X" or "O" marks.
    for row in board:
        for cell in row:
            if cell != 'X' and cell != 'O':
                return False
    return True

def is_valid_move(board, row, col):
    """Check if a move is valid"""
# Check if row and column are within valid range (1 to 3)
    if row < 1 or row > 3:
        return False
    if col < 1 or col > 3:
        return False
# Check if the cell is not already marked with 'X' or 'O'
    if board[row - 1][col - 1] in ('X', 'O'):
        return False
# If all checks passed, the move is valid
    return True

def make_move(board, player, row, col):
    """Make a move on the board"""
    board[row - 1][col - 1] = player

def computer_move(board):
    """Generate a random move for the computer"""
    while True:
        row = random.randint(1, 3)
        col = random.randint(1, 3)
        if is_valid_move(board, row, col): # line 63
            return row, col

def player_move(board, player):
    """ Get and validate player's move"""
# loop that keeps asking the player for a move until a valid move is provided.
    while True:
# starts a try-except block to handle potential errors during the input process.
        try:
            move = int(input(f"{player}, enter your move (1-9): "))
# calculates the row index | incremented by 1 to convert from 0-based indexing to 1-based indexing
            row = (move - 1) // 3 + 1
# calculates the remainder of division by 3 to find the column index | incremented by 1 to convert from 0-based indexing to 1-based indexing
            col = (move - 1) % 3 + 1
            if is_valid_move(board, row, col): # line 63
# checks if the calculated ROW and COLUMN indices correspond to a valid move | using PARAM board => is_valid_move function.
                return row, col # values as a tuple
# IF the move is not valid, this block is executed.
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            make_move(board, player, row, col) # line 76
        else:
# line generates a computer's move using the computer_move function, which generates a random move for the computer.
            row, col = computer_move(board) # line 80
# line updates the board with the computer's move using the make_move function.
            make_move(board, player, row, col) # line 76
# prints the updated game board
        print_board(board) # line 12
# TERNARY: If PLAYER is equal to 'X', then the new value of player will be 'O'. 
# Otherwise, if PLAYER is not equal to 'X', the new value of player will be 'X'.
# Means that, line switches the current player from 'X' to 'O', or from 'O' to 'X'.
        player = 'O' if player == 'X' else 'X'

def play_game():
    """This function encapsulates the main logic of playing the Tic Tac Toe game."""
# Initialize the board with numbers 1 to 9
    board = []  # Initialize an empty list to represent the board
    for i in range(3):  # Iterate over rows (i = 0, 1, 2)
        row = []  # Initialize an empty list to represent a row
        for j in range(3):  # Iterate over columns (j = 0, 1, 2)
            cell_value = 3 * i + j + 1  # Calculate the value for the cell
            cell_str = str(cell_value)  # Convert the value to a string
            row.append(cell_str)  # Add the string value to the current row
        board.append(row)  # Add the row to the board
# Initialize the current player as 'O'
    player = 'O'
# Print the initial board
    print_board(board) # line 12
# Computer's first move (always at the center)
    make_move(board, 'X', 2, 2) # line 76
# Print the updated board
    print_board(board) # line 12
# Main game loop
    while True:
# Check for a tie
        if is_tie(board): # line 54
            print("It's a tie!")
            break
# Check if the computer wins
        if the_winner_is(board, 'X'): # line 21
            print("Computer wins!")
            break
# Check if the player wins
        if the_winner_is(board, 'O'): # line 21
            print("You win!")
            break
# Player's move
        if player == 'O':
            row, col = player_move(board, player) # line 88
            make_move(board, player, row, col) # line 76
# Computer's move
        else:
            row, col = computer_move(board) # line 80
            make_move(board, player, row, col) # line 76
# Print the updated board, call function line 3
        print_board(board) # line 12
# Switch players (X to O, and vice versa)
        player = 'O' if player == 'X' else 'X'

if __name__ == "__main__":
    play_game() # line 120



# def the_winner_is(board, player):
#     """Check rows, columns, and diagonals for a win"""
# # Check rows for a win """A measure of how hard the control flow of a function is to understand. Functions with high Cognitive Complexity will be difficult to maintain."""
#     for row in board:
# # loop iterates through each row in the board list
#         row_match = True
#         for cell in row:
#             if cell != player:
#                 row_match = False
#                 break
#         if row_match:
#             return True
# # Check columns for a win
#     for col in range(3):
#         col_match = True
#         for row in range(3):
#             if board[row][col] != player:
#                 col_match = False
#                 break
#         if col_match:
#             return True
# # Check diagonals for a win
#     main_diag_match = True
#     anti_diag_match = True
#     for i in range(3):
#         if board[i][i] != player:
#             main_diag_match = False
#         if board[i][2 - i] != player:
#             anti_diag_match = False
#     if main_diag_match or anti_diag_match:
#         return True
#     return False