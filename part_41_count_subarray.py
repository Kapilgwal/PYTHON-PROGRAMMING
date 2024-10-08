from collections import defaultdict


def countSubarray(arr: list[int], k) -> int:
    cnt = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]

            if k == sum:
                cnt += 1
    return cnt


def countSubarrayBetter(arr, k):
    n = len(arr)  # size of the given array.
    mpp = defaultdict(int)
    preSum = 0
    cnt = 0

    mpp[0] = 1  # Setting 0 in the map.
    for i in range(n):
        # add current element to prefix Sum:
        preSum += arr[i]

        # Calculate x-k:
        remove = preSum - k

        # Add the number of subarrays to be removed:
        cnt += mpp[remove]

        # Update the count of prefix sum
        # in the map.
        mpp[preSum] += 1

    return cnt


def main():
    arr = [3, 1, 2, 4]
    k = 6
    ans1 = countSubarray(arr, k)
    ans2 = countSubarrayBetter(arr, k)
    print(ans1, ans2)


if __name__ == "__main__":
    main()
