from typing import List

def left_rotate_one(arr: List[int]):
    n = len(arr) - 1
    temp = arr[0]
    
    for i in range(1, n + 1):
        arr[i - 1] = arr[i]
    
    arr[n] = temp

def reverse(arr: List[int], low: int, high: int):
    while low < high:
        arr[low], arr[high] = arr[high], arr[low]  # Swap elements
        low += 1
        high -= 1

def left_rotate_one_best(arr: List[int]):
    k = 1  # Number of rotations
    reverse(arr, 0, len(arr) - 1)  # Reverse the entire array
    reverse(arr, 0, k - 1)         # Reverse the first part (0 to k-1)
    reverse(arr, k, len(arr) - 1)  # Reverse the remaining part (k to end)

def main():
    arr = [1, 2, 3, 4, 5, 6]
    print(f"Original array: {arr}")
    
    # left_rotate_one(arr)
    left_rotate_one_best(arr)
    
    print(f"After left rotating the array by one:\n{arr}")

if __name__ == "__main__":
    main()
