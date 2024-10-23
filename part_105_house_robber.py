import sys

def solveRec(arr: list[int], start: int, idx: int) -> int:
    if idx == start:
        return arr[start]

    if idx < start:
        return 0

    notTake = 0 + solveRec(arr, start, idx - 1)
    take = arr[idx] + solveRec(arr, start, idx - 2) if idx >= start + 2 else arr[idx]

    return max(notTake, take)

def maxNonAdjSumRec(arr: list[int]) -> int:
    n = len(arr)
    if n == 1:
        return arr[0]

    ans1 = solveRec(arr, 0, n - 2)
    ans2 = solveRec(arr, 1, n - 1)
    return max(ans1, ans2)


def solveMem(arr: list[int], start: int, idx: int, dp: list[int]) -> int:
    if idx == start:
        return arr[start]

    if idx < start:
        return 0

    if dp[idx] != -1:
        return dp[idx]

    notTake = 0 + solveMem(arr, start, idx - 1, dp)
    take = arr[idx] + solveMem(arr, start, idx - 2, dp) if idx >= start + 2 else arr[idx]

    dp[idx] = max(notTake, take)
    return dp[idx]

def maxNonAdjSumMem(arr: list[int]) -> int:
    n = len(arr)
    if n == 1:
        return arr[0]

    dp1 = [-1] * n
    dp2 = [-1] * n

    ans1 = solveMem(arr, 0, n - 2, dp1)
    ans2 = solveMem(arr, 1, n - 1, dp2)
    return max(ans1, ans2)


def solveTab(arr: list[int], start: int, end: int) -> int:
    n = len(arr)
    dp = [0] * (n)

    dp[start] = arr[start]

    for idx in range(start + 1, end + 1):
        notTake = dp[idx - 1]
        take = arr[idx] + dp[idx - 2] if idx >= start + 2 else arr[idx]
        dp[idx] = max(notTake, take)

    return dp[end]

def maxNonAdjSumTab(arr: list[int]) -> int:
    n = len(arr)
    if n == 1:
        return arr[0]

    ans1 = solveTab(arr, 0, n - 2)
    ans2 = solveTab(arr, 1, n - 1)
    return max(ans1, ans2)


def main():
    arr = [2, 3, 2]
    ans1 = maxNonAdjSumRec(arr)
    ans2 = maxNonAdjSumMem(arr)
    ans3 = maxNonAdjSumTab(arr)
    print(ans1, ans2, ans3)


if __name__ == "__main__":
    main()
