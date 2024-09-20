from typing import List


def merge(arr: List[int], low, mid, high):

    i = low
    j = mid + 1
    temp = []

    while i <= mid and j <= high:

        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1

        else:
            temp.append(arr[j])
            j += 1

    while i <= mid:

        temp.append(arr[i])
        i += 1

    while j <= high:
        
        temp.append(arr[j])
        j += 1
        
    # copying the element in main array 
    for i in range(low,high+1):
        arr[i] = temp[i - low]


def merge_sort(lst: List[int], low, high):

    if low >= high:
        return

    mid = (low + high) // 2

    merge_sort(lst, low, mid)
    merge_sort(lst, mid + 1, high)
    merge(lst, low, mid, high)


def main():
    lst = [3, 2, 6, 4, 7, 8, 5]
    print(lst)
    i = 0
    j = len(lst) - 1

    merge_sort(lst,i,j)
    print(lst)


if __name__ == "__main__":
    main()
