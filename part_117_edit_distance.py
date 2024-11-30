def solveRec(s1: str, s2: str, i: int, j: int) -> int:
    if i < 0:
        return j + 1

    if j < 0:
        return i + 1

    if s1[i] == s2[j]:
        return solveRec(s1, s2, i - 1, j - 1)

    else:
        replace = 1 + solveRec(s1, s2, i - 1, j - 1)
        delete = 1 + solveRec(s1, s2, i - 1, j)
        insert = 1 + solveRec(s1, s2, i, j - 1)
        return min(replace, delete, insert)


def minOper(s1: str, s2: str):
    n = len(s1)
    m = len(s2)

    ans = solveRec(s1, s2, n - 1, m - 1)
    return ans


def main():
    s1 = "horse"
    s2 = "ros"

    ans = minOper(s1, s2)
    print(ans)


if __name__ == "__main__":
    main()
