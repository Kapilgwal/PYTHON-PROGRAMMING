def solve(
    row: int,
    col: int,
    m: list[list[int]],
    n: int,
    ans: list[str],
    temp: str,
    vis: list[list[int]],
):
    if row == n - 1 and col == n - 1:
        ans.append(temp)
        return

    # Mark the current cell as visited
    vis[row][col] = 1

    # Move Down
    if row + 1 < n and m[row + 1][col] == 1 and vis[row + 1][col] == 0:
        solve(row + 1, col, m, n, ans, temp + "D", vis)

    # Move Left
    if col - 1 >= 0 and m[row][col - 1] == 1 and vis[row][col - 1] == 0:
        solve(row, col - 1, m, n, ans, temp + "L", vis)

    # Move Right
    if col + 1 < n and m[row][col + 1] == 1 and vis[row][col + 1] == 0:
        solve(row, col + 1, m, n, ans, temp + "R", vis)

    # Move Up
    if row - 1 >= 0 and m[row - 1][col] == 1 and vis[row - 1][col] == 0:
        solve(row - 1, col, m, n, ans, temp + "U", vis)

    # Backtrack
    vis[row][col] = 0


def ratInMaze(n: int, m: list[list[int]]) -> list[str]:
    if m[0][0] == 0 or m[n - 1][n - 1] == 0:
        return ["Path does not exist"]

    ans = []
    temp = ""
    vis = [[0 for _ in range(n)] for _ in range(n)]
    solve(0, 0, m, n, ans, temp, vis)
    return ans


def main():
    N = 4
    m = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
    ans = ratInMaze(N, m)
    print(ans)


if __name__ == "__main__":
    main()
