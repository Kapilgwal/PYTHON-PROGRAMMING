def isSafe(row: int, col: int, board: list[list[str]], n: int) -> bool:
    duprow = row
    dupcol = col

    # Check upper diagonal on the left
    while row >= 0 and col >= 0:
        if board[row][col] == "Q":
            return False
        row -= 1
        col -= 1

    # Check left row
    row = duprow
    col = dupcol
    while col >= 0:
        if board[row][col] == "Q":
            return False
        col -= 1

    # Check lower diagonal on the left
    col = dupcol
    while row < n and col >= 0:
        if board[row][col] == "Q":
            return False
        row += 1
        col -= 1

    return True


def solve(idx: int, board: list[list[str]], ans: list[list[list[str]]], n: int):
    if idx == n:
        # Append a deep copy of the board
        ans.append([row[:] for row in board])
        return

    for row in range(n):
        if isSafe(row, idx, board, n):
            board[row][idx] = "Q"  # Place queen
            solve(idx + 1, board, ans, n)  # Recur for next column
            board[row][idx] = "."  # Backtrack


def n_queen(n: int) -> list[list[str]]:
    ans = []
    # Initialize the board with '.'
    board = [["." for _ in range(n)] for _ in range(n)]
    solve(0, board, ans, n)
    return ans


def main():
    n = 4
    ans = n_queen(n)
    # Format and print the result
    for solution in ans:
        for row in solution:
            print(" ".join(row))
        print("\n")


if __name__ == "__main__":
    main()
