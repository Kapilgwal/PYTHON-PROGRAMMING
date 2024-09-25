def longest_subarray_sum_length(arr: list[int], k: int) -> int:
    max_len = 0
    n = len(arr)

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            if current_sum == k:
                cur_len = j - i + 1
                max_len = max(max_len, cur_len)
    
    return max_len

def longest_subarray_sum_length_better(a : list[int], k : int) -> int:
    n = len(a) # size of the array.

    preSumMap = {}
    Sum = 0
    maxLen = 0
    for i in range(n):
        # calculate the prefix sum till index i:
        Sum += a[i]

        # if the sum = k, update the maxLen:
        if Sum == k:
            maxLen = max(maxLen, i + 1)

        # calculate the sum of remaining part i.e. x-k:
        rem = Sum - k

        # Calculate the length and update maxLen:
        if rem in preSumMap:
            length = i - preSumMap[rem]
            maxLen = max(maxLen, length)

        # Finally, update the map checking the conditions:
        if Sum not in preSumMap:
            preSumMap[Sum] = i

    return maxLen

def main():
    N = 3
    k = 1
    array = [-1,1,1]
    length1 = longest_subarray_sum_length(array, k)
    length2 = longest_subarray_sum_length_better(array, k)
    print(length1,length2)

if __name__ == "__main__":
    main()
