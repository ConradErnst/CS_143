import random
import time

class SudokuBoard:
    def __init__(self, board):
        self.board = board

    # Display the auto generated board to the terminal
    def print_board(self):
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - - ")
            for j in range(len(self.board[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")
                if j == 8:
                    print(self.board[i][j])
                else:
                    print(str(self.board[i][j]) + " ", end="")


def generate_board():
    # Create a solved board
    board = [[(i*3 + i//3 + j) % 9 + 1 for j in range(9)] for i in range(9)]

    # Shuffle the board while maintaining the rules of Sudoku
    for i in range(81):
        row1, col1 = divmod(i, 9)
        row2 = random.randint(0, 8)
        col2 = random.randint(0, 8)
        board[row1][col1], board[row2][col2] = board[row2][col2], board[row1][col1]
        if not is_valid_move(board, row1, col1, board[row1][col1]) or not is_valid_move(board, row2, col2, board[row2][col2]):
            board[row1][col1], board[row2][col2] = board[row2][col2], board[row1][col1]

    # Remove cells to simulate Medium difficulty mode
    for i in range(81):
        row, col = divmod(i, 9)
        val = board[row][col]
        board[row][col] = 0
        if not is_unique_solution(board):
            board[row][col] = val

    # Create the Sudoku board object and return it
    return SudokuBoard(board)


def is_unique_solution(board):
    # Find an empty cell to fill
    row, col = find_empty_cell(board)
    if row == -1 and col == -1:
        # The board is solved
        return True

    # Try each possible value in the empty cell
    for val in range(1, 10):
        if is_valid_move(board, row, col, val):
            board[row][col] = val
            if not is_unique_solution(board):
                board[row][col] = 0
                return False
            board[row][col] = 0

    return True


def solve_board(board, count):
    # Find an empty cell to fill
    row, col = find_empty_cell(board)
    if row == -1 and col == -1:
        # The board is solved
        return True, count

    # Try each possible value in the empty cell
    for val in range(1, 10):
        if is_valid_move(board, row, col, val):
            board[row][col] = val
            if solve_board(board, count):
                return True, count
            board[row][col] = 0

    # Backtrack
    count += 1
    return False, count


def find_empty_cell(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j
    return -1, -1


def is_valid_move(board, row, col, val):
    # Check if the value is already in the same row or column
    for i in range(9):
        if board[row][i] == val:
            return False
        if board[i][col] == val:
            return False

    # Check if the value is already in the same 3x3 box
    box_row = row // 3
    box_col = col // 3
    for i in range(box_row * 3, box_row * 3 + 3):
        for j in range(box_col * 3, box_col * 3 + 3):
            if board[i][j] == val:
                return False

    return True


def main():
    board = generate_board()
    # print("Sudoku Board:")
    # board.print_board()

    # start_time = time.time()
    # solved, count = solve_board(board.board, 0)
    # end_time = time.time()

    # if solved:
    #     print("\nSolved Sudoku Board:")
    #     board.print_board()
    #     print(f"\nTime taken to solve the board: {round(end_time - start_time, 2)} seconds")
    #     print(f"Total number of moves: {count}")

if __name__ == '__main__':
    main()