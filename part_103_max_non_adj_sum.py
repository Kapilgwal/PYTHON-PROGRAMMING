import sys


def solveRec(arr: list[int], idx: int) -> int:
    if idx == 0:
        return arr[0]

    if idx < 0:
        return -sys.maxsize

    notTake = 0 + solveRec(arr, idx - 1)
    take = 0
    if idx > 1:
        take = arr[idx] + solveRec(arr, idx - 2)

    return max(notTake, take)


def maxNonAdjSumRec(arr: list[int]) -> int:
    n = len(arr)
    ans = solveRec(arr, n - 1)
    return ans


def solveMem(arr: list[int], idx: int, dp: list[int]) -> int:
    if idx == 0:
        return arr[0]

    if idx < 0:
        return -sys.maxsize

    if dp[idx] != -1:
        return dp[idx]

    notTake = 0 + solveMem(arr, idx - 1, dp)
    take = 0
    if idx > 1:
        take = arr[idx] + solveMem(arr, idx - 2, dp)

    dp[idx] = max(notTake, take)
    return dp[idx]


def maxNonAdjSumMem(arr: list[int]) -> int:
    n = len(arr)
    dp = [-1 for _ in range(n + 1)]
    ans = solveMem(arr, n - 1, dp)
    return ans


def solveTab(arr: list[int]) -> int:
    n = len(arr)
    if n == 0:
        return 0
    dp = [0 for _ in range(n)]
    dp[0] = arr[0]

    for idx in range(1, n):
        notTake = dp[idx - 1]
        take = arr[idx]
        if idx > 1:
            take += dp[idx - 2]
        dp[idx] = max(notTake, take)

    return dp[n - 1]


def maxNonAdjSumTab(arr: list[int]) -> int:
    ans = solveTab(arr)
    return ans


def solveOpm(arr: list[int]) -> int:
    n = len(arr)
    if n == 0:
        return 0

    prev1 = arr[0]
    prev2 = 0

    for idx in range(1, n):
        notTake = prev1
        take = arr[idx]
        if idx > 1:
            take += prev2
        curr = max(notTake, take)

        prev2 = prev1
        prev1 = curr

    return prev1


def maxNonAdjSumOpm(arr: list[int]) -> int:
    ans = solveOpm(arr)
    return ans


def main():
    arr = [1, 2, 3, 1, 3, 5, 8, 1, 9]
    ans1 = maxNonAdjSumRec(arr)
    ans2 = maxNonAdjSumMem(arr)
    ans3 = maxNonAdjSumTab(arr)
    ans4 = maxNonAdjSumOpm(arr)
    print(ans1, ans2, ans3, ans4)


if __name__ == "__main__":
    main()
