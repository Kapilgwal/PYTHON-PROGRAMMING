def find_number_of_LIS(arr):
    n = len(arr)

    dp = [1] * n
    count = [1] * n

    maxi = 1

    for i in range(n):
        for prev_index in range(i):
            if arr[prev_index] < arr[i] and dp[prev_index] + 1 > dp[i]:
                dp[i] = dp[prev_index] + 1
                count[i] = count[prev_index]
            elif arr[prev_index] < arr[i] and dp[prev_index] + 1 == dp[i]:
                count[i] += count[prev_index]
        
        maxi = max(maxi, dp[i])

    num_of_LIS = 0

    for i in range(n):
        if dp[i] == maxi:
            num_of_LIS += count[i]

    return num_of_LIS


if __name__ == "__main__":
    arr = [1, 5, 4, 3, 2, 6, 7, 2]

    print("The count of Longest Increasing Subsequences is:", find_number_of_LIS(arr))