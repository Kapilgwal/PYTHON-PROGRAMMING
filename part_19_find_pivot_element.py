def findPivotElement(arr: list[int]) -> int:
    n = len(arr)

    for i in range(1, n - 1):
        if all(arr[j] < arr[i] for j in range(i)):
            if all(arr[k] > arr[i] for k in range(i + 1, n)):
                return i

    return -1

def main():
    arr = [5, 1, 4, 3, 6, 8, 10, 7, 9]
    ans = findPivotElement(arr)
    print(ans)

if __name__ == "__main__":
    main()
