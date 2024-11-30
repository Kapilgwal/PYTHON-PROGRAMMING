prime = int(1e9 + 7)


def countUtil(s1, s2, ind1, ind2, dp):
    if ind2 < 0:
        return 1
    if ind1 < 0:
        return 0

    if dp[ind1][ind2] != -1:
        return dp[ind1][ind2]

    if s1[ind1] == s2[ind2]:
        leaveOne = countUtil(s1, s2, ind1 - 1, ind2 - 1, dp)
        stay = countUtil(s1, s2, ind1 - 1, ind2, dp)

        dp[ind1][ind2] = (leaveOne + stay) % prime
        return dp[ind1][ind2]
    else:
        dp[ind1][ind2] = countUtil(s1, s2, ind1 - 1, ind2, dp)
        return dp[ind1][ind2]


def subsequenceCounting(s1, s2, lt, ls):
    dp = [[-1 for j in range(ls)] for i in range(lt)]

    return countUtil(s1, s2, lt - 1, ls - 1, dp)


def main():
    s1 = "babgbag"
    s2 = "bag"

    print(
        "The Count of Distinct Subsequences is",
        subsequenceCounting(s1, s2, len(s1), len(s2)),
    )


if __name__ == "__main__":
    main()
