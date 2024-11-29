def solveRec(text1: str, text2: str, ptr1: int, ptr2: int, n1: int, n2: int) -> int:
    if ptr1 == n1 or ptr2 == n2:
        return 0

    if text1[ptr1] == text2[ptr2]:
        return 1 + solveRec(text1, text2, ptr1 + 1, ptr2 + 1, n1, n2)

    else:
        return max(
            solveRec(text1, text2, ptr1 + 1, ptr2, n1, n2),
            solveRec(text1, text2, ptr1, ptr2 + 1, n1, n2),
        )


def longestPalindromeSubsequence(text: str) -> int:
    text1 = text
    text2 = text[::-1]

    ptr1 = 0
    ptr2 = 0
    ans = solveRec(text1, text2, ptr1, ptr2, len(text1), len(text2))
    return ans


def main():
    text = "bbabcbcab"
    ans = longestPalindromeSubsequence(text)
    print(ans)


if __name__ == "__main__":
    main()
