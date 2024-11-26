def solveRec(arr: list[int], prev: int, curr: int, n: int) -> int:

    if curr >= n:
        return 0

    if prev == -1 or arr[curr] % arr[prev] == 0 or arr[prev] % arr[curr] == 0:
        return 1 + solveRec(arr, curr, curr + 1, n)

    else:
        return solveRec(arr, prev, curr + 1, n)


def longestDivisibleSubsetRec(arr: list[int]) -> int:
    n = len(arr)
    prev = -1
    curr = 0

    ans = solveRec(arr, prev, curr, n)
    return ans


def solveMem(arr: list[int], prev: int, curr: int, n: int, dp: list[list[int]]) -> int:

    if curr >= n:
        return 0

    if dp[curr][prev] != -1:
        return dp[curr][prev]

    if prev == -1 or arr[curr] % arr[prev] == 0 or arr[prev] % arr[curr] == 0:
        dp[curr][prev] = 1 + solveMem(arr, curr, curr + 1, n, dp)
        return dp[curr][prev]

    else:
        dp[curr][prev] = solveMem(arr, prev, curr + 1, n, dp)
        return dp[curr][prev]


def longestDivisibleSubsetMem(arr: list[int]) -> int:
    n = len(arr)
    prev = -1
    curr = 0
    dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
    ans = solveMem(arr, prev, curr, n, dp)
    return ans


def solveTab(arr: list[int], n: int) -> int:

    dp = [1] * n
    max_length = 1
    for curr in range(1, n):
        for prev in range(curr):
            if arr[curr] % arr[prev] == 0 or arr[prev] % arr[curr] == 0:
                dp[curr] = max(dp[curr], dp[prev] + 1)
        max_length = max(max_length, dp[curr]) 

    return max_length



def longestDivisibleSubsetTab(arr: list[int]) -> int:
    n = len(arr)
    ans = solveTab(arr, n)
    return ans


def main():
    arr = [1, 16, 7, 8, 4]
    ans1 = longestDivisibleSubsetRec(arr)
    ans2 = longestDivisibleSubsetMem(arr)
    ans3 = longestDivisibleSubsetTab(arr)
    print(ans1, ans2, ans3)


if __name__ == "__main__":
    main()
