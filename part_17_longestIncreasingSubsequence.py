def lower_bound(temp: list[int], num: int) -> int:
    low = 0
    high = len(temp)

    while low < high:
        mid = low + (high - low) // 2

        if temp[mid] < num:
            low = mid + 1
        else:
            high = mid
            
    return low


def longestIncreasingSubsequence(arr: list[int], n: int) -> int:
    if n == 0:  # Handle edge case for empty array
        return 0

    temp = [arr[0]]
    lis_length = 1

    for i in range(1, n):
        if arr[i] > temp[-1]:
            temp.append(arr[i])
            lis_length += 1
        else:
            ind = lower_bound(temp, arr[i])
            temp[ind] = arr[i]

    return lis_length


def main():
    arr = [10, 9, 2, 5, 3, 7, 101, 18]  # Provide a valid input array
    ans = longestIncreasingSubsequence(arr, len(arr))
    print(f"The length of the longest increasing subsequence is: {ans}")


if __name__ == "__main__":
    main()
