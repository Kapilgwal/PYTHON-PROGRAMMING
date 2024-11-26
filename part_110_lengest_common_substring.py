def solve(s1: str, s2: str, i: int, j: int, count: int, n1: int, n2: int) -> int:

    if i >= n1 or j >= n2:
        return count
    if s1[i] == s2[j]:
        count = solve(s1, s2, i + 1, j + 1, count + 1, n1, n2)

    return max(count, solve(s1, s2, i + 1, j, 0, n1, n2), solve(s1, s2, i, j + 1, 0, n1, n2))


def longestCommonSubstring(s1: str, s2: str) -> int:

    n1, n2 = len(s1), len(s2)
    return solve(s1, s2, 0, 0, 0, n1, n2)


def lcs(s1, s2):
    n = len(s1)
    m = len(s2)
    
    # Create a DP table with dimensions (n+1) x (m+1) initialized to zeros
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Initialize a variable 'ans' to keep track of the maximum LCS length
    ans = 0
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                # If the characters match, increment LCS length by 1
                val = 1 + dp[i - 1][j - 1]
                dp[i][j] = val
                ans = max(ans, val)
            else:
                # If the characters do not match, reset LCS length to zero
                dp[i][j] = 0
    
    # 'ans' contains the length of the Longest Common Substring
    return ans


def main():
    s1 = "abcjklp"
    s2 = "acjkp"
    ans = longestCommonSubstring(s1, s2)
    ans2 = lcs(s1,s2)
    print("Length of the longest common substring is:", ans,ans2)


if __name__ == "__main__":
    main()


"""

abcaa
aacba

2 changes or 2 insertions


"""