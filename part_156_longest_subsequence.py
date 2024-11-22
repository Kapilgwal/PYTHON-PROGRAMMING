def recursion(arr: list[int], prev: int, curr: int) -> int:
    if curr >= len(arr):
        return 0

    notTake = recursion(arr, prev, curr + 1)

    take = 0
    if prev == -1 or arr[curr] > arr[prev]:
        take = 1 + recursion(arr, curr, curr + 1)

    return max(notTake, take)


def longestSubsequence(arr: list[int]) -> int:
    return recursion(arr, -1, 0)


def memorization(arr: list[int], prev: int, curr: int, dp: list[list[int]]) -> int:
    if curr >= len(arr):
        return 0

    if dp[curr][prev + 1] != -1:
        return dp[curr][prev + 1]

    notTake = memorization(arr, prev, curr + 1, dp)

    take = 0
    if prev == -1 or arr[curr] > arr[prev]:
        take = 1 + memorization(arr, curr, curr + 1, dp)

    dp[curr][prev + 1] = max(notTake, take)
    return dp[curr][prev + 1]


def longestSubsequenceMemo(arr: list[int]) -> int:
    n = len(arr)
    dp = [[-1 for _ in range(n + 1)] for _ in range(n)]
    return memorization(arr, -1, 0, dp)


def tabulation(arr: list[int], n: int) -> int:
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for curr in range(n - 1, -1, -1):
        for prev in range(curr - 1, -2, -1):
            notTake = dp[curr + 1][prev + 1]

            take = 0
            if prev == -1 or arr[curr] > arr[prev]:
                take = 1 + dp[curr + 1][curr + 1]

            dp[curr][prev + 1] = max(notTake, take)

    return dp[0][0]


def longestSubsequenceTab(arr: list[int]) -> int:
    n = len(arr)
    return tabulation(arr, n)


def main():
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    ans1 = longestSubsequence(arr)
    ans2 = longestSubsequenceMemo(arr)
    ans3 = longestSubsequenceTab(arr)
    print(ans1, ans2, ans3)


if __name__ == "__main__":
    main()
