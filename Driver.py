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
    board = [[0 for _ in range(9)] for _ in range(9)]
    fill_board(board)
    replace_tiles(board)
    return SudokuBoard(board)

def fill_board(board):
    row, col = find_empty_cell(board)
    if row == -1:
        return True

    numbers = list(range(1, 10))
    random.shuffle(numbers)
    for num in numbers:
        if is_valid_move(board, row, col, num):
            board[row][col] = num
            if fill_board(board):
                return True
            board[row][col] = 0

    return False

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

def replace_tiles(board):
    count = 0
    while count < 56:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0
            count += 1

def solve_board(board, count):
    row, col = find_empty_cell(board)
    if row == -1:
        return True, count

    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            board[row][col] = num
            solved, count = solve_board(board, count+1)
            if solved:
                return True, count
            board[row][col] = 0

    return False, count


def main():
    board = generate_board()
    print("Sudoku Board:")
    board.print_board()

    start_time = time.time()
    solved, count = solve_board(board.board, 0)
    end_time = time.time()

    if solved:
        print("\nSolved Sudoku Board:")
        board.print_board()
        print(f"\nTime taken to solve the board: {round(end_time - start_time, 2)} seconds")
        print(f"Total number of moves: {count}")

if __name__ == '__main__':
    main()