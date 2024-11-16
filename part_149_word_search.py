def search_next(board, word, row, col, index, m, n):
    # If index reaches the length of the word, the word is found
    if index == len(word):
        return True

    # Check boundaries and if the current cell matches the current character
    if row < 0 or col < 0 or row >= m or col >= n or board[row][col] != word[index] or board[row][col] == '!':
        return False

    # Temporarily mark the cell as visited
    char = board[row][col]
    board[row][col] = '!'

    # Explore all four directions
    top = search_next(board, word, row - 1, col, index + 1, m, n)
    right = search_next(board, word, row, col + 1, index + 1, m, n)
    bottom = search_next(board, word, row + 1, col, index + 1, m, n)
    left = search_next(board, word, row, col - 1, index + 1, m, n)

    # Undo the visit marking
    board[row][col] = char

    return top or right or bottom or left

def exist(board, word):
    m = len(board)
    n = len(board[0])

    # Start searching for the word
    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:  # First character match
                if search_next(board, word, i, j, 0, m, n):
                    return True

    return False

# Test the function
board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

word = "ABCCEDS"
res = exist(board, word)
if res:
    print("True")
else:
    print("False")
