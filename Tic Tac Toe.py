

import random
import os

def create_board():
    """Returns a fresh 3x3 empty board."""
    return [[' ' for _ in range(3)] for _ in range(3)]


def display_board(board):
    """Prints the current state of the board."""
    os.system('cls' if os.name == 'nt' else 'clear')   # Clear terminal screen

    print("\n ===  TIC TAC TOE  === \n")
    print("     Col1  Col2  Col3")
    print("     ─────────────────")

    row_labels = ["Row1", "Row2", "Row3"]

    for i in range(3):
        print(f" {row_labels[i]}│  {board[i][0]}  │  {board[i][1]}  │  {board[i][2]}  │")
        if i < 2:
            print("     ─────────────────")

    print("     ─────────────────")
    print("\n  Positions: (row, col) from 1 to 3\n")



def make_move(board, row, col, player):
    """
    Places the player's symbol on the board.
    Returns True if the move was successful, False if cell is already taken.
    """
    if board[row][col] == ' ':     # Check if cell is empty
        board[row][col] = player   # Place player symbol
        return True
    else:
        print("⚠️  That cell is already taken! Try another.")
        return False



def check_winner(board, player):
    """
    
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True

    # --- Check all 3 Columns ---
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    # --- Check Main Diagonal (top-left to bottom-right) ---
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True

    # --- Check Anti-Diagonal (top-right to bottom-left) ---
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False   # No winner found


# ─────────────────────────────────────────────
# STEP 5: Check for a Draw
# Board is full with no winner = Draw
# ─────────────────────────────────────────────
def check_draw(board):
    """Returns True if the board is completely filled (no empty cells)."""
    for row in board:
        if ' ' in row:   # If any cell is still empty, game continues
            return False
    return True   # All cells filled = Draw


# ─────────────────────────────────────────────
# STEP 6: Get Player Input (with Validation)
# Keeps asking until the player gives valid input
# ─────────────────────────────────────────────
def get_player_move(board, player):
    """
    Asks the current player to enter a valid row and column.
    Validates: must be 1-3, and cell must be empty.
    """
    while True:
        try:
            print(f" 🎮 Player {player}'s Turn")
            row = int(input("    Enter Row    (1-3): ")) - 1   # Convert to 0-index
            col = int(input("    Enter Column (1-3): ")) - 1   # Convert to 0-index

            # Check if within valid range
            if row not in range(3) or col not in range(3):
                print("⚠️  Invalid! Row and Column must be between 1 and 3.\n")
                continue

            # Try to place the move
            if make_move(board, row, col, player):
                return   # Move successful, exit loop

        except ValueError:
            # Handles non-number input like letters or symbols
            print("⚠️  Please enter a NUMBER (1, 2, or 3).\n")


# ─────────────────────────────────────────────
# STEP 7: Simple AI (Computer) Move
# AI picks a random empty cell
# ─────────────────────────────────────────────
def get_ai_move(board, ai_symbol):
    """
    AI finds all empty cells and picks one randomly.
    This is a beginner-level AI (no strategy).
    """
    empty_cells = []

    # Collect all positions where the cell is empty
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                empty_cells.append((row, col))

    if empty_cells:
        row, col = random.choice(empty_cells)   # Pick random empty cell
        print(f"\n 🤖 Computer (O) places at Row {row+1}, Col {col+1}")
        input("    Press Enter to continue...")
        make_move(board, row, col, ai_symbol)


# ─────────────────────────────────────────────
# STEP 8: Main Game Loop
# Ties everything together
# ─────────────────────────────────────────────
def play_game(vs_computer=False):
    """
    Runs one full game session.
    vs_computer = True  → Player vs AI
    vs_computer = False → Player vs Player
    """
    board = create_board()
    players = ['X', 'O']
    current = 0   # Index: 0 = X's turn, 1 = O's turn

    while True:
        player = players[current]
        display_board(board)

        # ── Get Move ──
        if vs_computer and player == 'O':
            get_ai_move(board, 'O')   # AI plays as 'O'
        else:
            get_player_move(board, player)

        # ── Check Win ──
        if check_winner(board, player):
            display_board(board)
            if vs_computer and player == 'O':
                print(" 🤖 Computer (O) wins! Better luck next time!\n")
            else:
                print(f" 🏆 Player {player} WINS! Congratulations!\n")
            break

        # ── Check Draw ──
        if check_draw(board):
            display_board(board)
            print(" 🤝 It's a DRAW! Great game!\n")
            break

        # ── Switch Turn ──
        current = 1 - current   # Toggles between 0 and 1


# ─────────────────────────────────────────────
# STEP 9: Main Menu
# Entry point of the program
# ─────────────────────────────────────────────
def main():
    """Main menu - lets user choose game mode and play again."""
    print("\n" + "="*40)
    print("      WELCOME TO TIC TAC TOE!")
    print("="*40)

    while True:
        print("\n  Select Mode:")
        print("  1. Player vs Player  (2 humans)")
        print("  2. Player vs Computer (AI)")
        print("  3. Exit\n")

        choice = input("  Enter your choice (1/2/3): ").strip()

        if choice == '1':
            play_game(vs_computer=False)
        elif choice == '2':
            play_game(vs_computer=True)
        elif choice == '3':
            print("\n  Thanks for playing! Goodbye! 👋\n")
            break
        else:
            print("  ⚠️  Invalid choice! Enter 1, 2, or 3.")

        # Ask to play again
        again = input("\n  Play again? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            print("\n  Thanks for playing! Goodbye! 👋\n")
            break


# ─────────────────────────────────────────────
# Program Entry Point
# This runs only when the file is executed directly
# ─────────────────────────────────────────────
if __name__ == "__main__":
    main()