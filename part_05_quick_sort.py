from typing import List

def partition(arr: List[int], low, high):
    pivot = arr[low]  # Set pivot as the first element
    left = low + 1  # Start from the next element after pivot
    right = high

    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] > pivot:
            right -= 1

        if left > right:  # When pointers cross, partition is done
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]  # Swap

    # Place pivot element in the correct position
    arr[low], arr[right] = arr[right], arr[low]
    return right

def quick_sort(lst: List[int], low, high):
    if low >= high:
        return
    pi = partition(lst, low, high)  # Partition the array
    quick_sort(lst, low, pi - 1)  # Sort the left half
    quick_sort(lst, pi + 1, high)  # Sort the right half

def main():
    lst = [3, 2, 6, 4, 7, 8, 5]
    print("Before Sorting:", lst)
    i = 0
    j = len(lst) - 1

    quick_sort(lst, i, j)
    print("After Sorting:", lst)

if __name__ == "__main__":
    main()
