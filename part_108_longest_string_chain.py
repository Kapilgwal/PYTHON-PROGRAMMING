def isSequence(str1: str, str2: str) -> bool:
    if len(str1) != len(str2) + 1:
        return False

    i, j = 0, 0
    while i < len(str1) and j < len(str2):
        if str1[i] == str2[j]:
            j += 1
        i += 1

    return j == len(str2)

def solveRec(words: list[str], curr: int, prev: int, n: int) -> int:
    if curr == n:
        return 0

    include = 0
    if prev == -1 or isSequence(words[curr], words[prev]):
        include = 1 + solveRec(words, curr + 1, curr, n)

    exclude = solveRec(words, curr + 1, prev, n)

    return max(include, exclude)

def longestStringChain(words: list[str]) -> int:
    words.sort(key=len) 
    n = len(words)
    return solveRec(words, 0, -1, n)

def main():
    words = ["a", "b", "ba", "bca", "bda", "bdca"]
    ans = longestStringChain(words)
    print(ans)

if __name__ == "__main__":
    main()
