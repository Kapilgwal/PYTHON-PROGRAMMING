def isAllStars(str1: str, i: int):

    for j in range(i + 1):
        if str1[j] != "*":
            return False

    return True


def solveRec(str1: str, str2: str, i: int, j: int) -> int:

    if i < 0 and j < 0:
        return True

    if i < 0 and j >= 0:
        return False

    if j < 0 and i >= 0:
        return isAllStars(str1, i)

    if str1[i] == str2[j] or str1[i] == "?":
        return solveRec(str1, str2, i - 1, j - 1)

    else:
        if str1[i] == "*":
            return solveRec(str1, str2, i - 1, j) or solveRec(str1, str2, i, j - 1)

        else:
            return False


def isMatch(str1: str, str2: str):
    n = len(str1)
    m = len(str2)

    ans = solveRec(str1, str2, n - 1, m - 1)
    return ans


def main():
    str1 = "?ay"
    str2 = "ray"

    ans = isMatch(str1, str2)
    print(ans)


if __name__ == "__main__":
    main()
