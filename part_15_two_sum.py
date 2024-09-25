def twoSum(arr: list[int], k: int) -> int:

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == k:
                return True

    return False

def twoSumBetter(arr: list[int], k: int) -> int:

    for i in range(len(arr)):
        if k - arr[i]:
            return True

    return False

def twoSumBest(arr : list[int], k : int) -> int:
    arr.sort()
    
    left = 0
    right = len(arr) - 1
    
    while left < right:
        if arr[left] + arr[right] == k:
            return True
        
        elif arr[left] + arr[right] > k:
            right -= 1
        
        else:
            left += 1

    return False 


def main():
    N = 3
    k = 14
    array = [2, 6, 5, 8, 11]
    print(twoSum(array, k))
    print(twoSumBetter(array, k))
    print(twoSumBest(array, k))


if __name__ == "__main__":
    main()
