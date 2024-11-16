def isValid(board: list[list[str]], row: int, col: int, c: str):

    for i in range(0, 9):
        if board[i][col] == c:
            return False
        if board[row][i] == c:
            return False
        if board[3 * (row // 3) + i//3][3 * (col // 3) + i % 3] == c:
            return False
    return True


def solveSudoko(board: list[list[str]]):

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ".":
                for k in range(1, 10):
                    if isValid(board, i, j, str(k)):
                        board[i][j] = str(k)

                        if solveSudoko(board):
                            return True
                        else:
                            board[i][j] = "."

                return False

    return True


def main():
    board = [
        ["9", "5", "7", ".", "1", "3", ".", "8", "4"],
        ["4", "8", "3", ".", "5", "7", "1", ".", "6"],
        [".", "1", "2", ".", "4", "9", "5", "3", "7"],
        ["1", "7", ".", "3", ".", "4", "9", ".", "2"],
        ["5", ".", "4", "9", "7", ".", "3", "6", "."],
        ["3", ".", "9", "5", ".", "8", "7", ".", "1"],
        ["8", "4", "5", "7", "9", ".", "6", "1", "3"],
        [".", "9", "1", ".", "3", "6", ".", "7", "5"],
        ["7", ".", "6", "1", "8", "5", "4", ".", "9"],
    ]

    solveSudoko(board)
    print(board)


if __name__ == "__main__":
    main()
