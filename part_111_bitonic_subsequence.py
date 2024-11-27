def bitonicSubsequence(arr: list[int]) -> int:
    """Find the length of the longest bitonic subsequence."""
    n = len(arr)
    if n == 0:
        return 0

    # Step 1: Compute LIS for each element
    lis = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                lis[i] = max(lis[i], lis[j] + 1)

    # Step 2: Compute LDS for each element
    lds = [1] * n
    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                lds[i] = max(lds[i], lds[j] + 1)

    # Step 3: Combine LIS and LDS to find the maximum bitonic subsequence length
    max_bitonic = 0
    for i in range(n):
        max_bitonic = max(max_bitonic, lis[i] + lds[i] - 1)

    return max_bitonic


def main():
    arr = [1, 11, 2, 10, 4, 5, 2, 1]
    ans = bitonicSubsequence(arr)
    print("Length of the longest bitonic subsequence is:", ans)


if __name__ == "__main__":
    main()
