import sys

def solveRec(heights: list[int], index: int, k: int) -> int:
    if index == 0:
        return 0

    mini = sys.maxsize

    for i in range(1, k + 1):
        if index - i >= 0:  # Ensure index is valid
            temp = abs(heights[index] - heights[index - i]) + solveRec(heights, index - i, k)
            mini = min(mini, temp)
    
    return mini

def minEnergyRec(heights: list[int], k: int) -> int:
    n = len(heights)
    ans = solveRec(heights, n - 1, k)
    return ans


def solveMem(heights: list[int], index: int, k: int, dp: list[int]) -> int:
    if index == 0:
        return 0

    if dp[index] != -1:
        return dp[index]

    mini = sys.maxsize

    for i in range(1, k + 1):
        if index - i >= 0:  # Ensure index is valid
            temp = abs(heights[index] - heights[index - i]) + solveMem(heights, index - i, k, dp)
            mini = min(mini, temp)

    dp[index] = mini
    return dp[index]

def minEnergyMem(heights: list[int], k: int) -> int:
    n = len(heights)
    dp = [-1 for _ in range(n)]
    ans = solveMem(heights, n - 1, k, dp)
    return ans


def solveTab(heights: list[int], k: int) -> int:
    n = len(heights)
    dp = [0 for _ in range(n)]
    dp[0] = 0

    for index in range(1, n):
        mini = sys.maxsize
        for i in range(1, k + 1):
            if index - i >= 0:  # Ensure index is valid
                temp = dp[index - i] + abs(heights[index] - heights[index - i])
                mini = min(mini, temp)
        dp[index] = mini

    return dp[n - 1]

def minEnergyTab(heights: list[int], k: int) -> int:
    ans = solveTab(heights, k)
    return ans


def main():
    heights = [10, 20, 30, 10]
    k = 2  # Example jump length
    ans1 = minEnergyRec(heights, k)
    ans2 = minEnergyMem(heights, k)
    ans3 = minEnergyTab(heights, k)
    print(ans1, ans2, ans3)


if __name__ == "__main__":
    main()
