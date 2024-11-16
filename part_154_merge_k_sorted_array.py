import heapq

def mergeKSortedArray(arr: list[list[int]]):
    heap = []
    result = []

    for i in range(len(arr)):
        if arr[i]:
            heapq.heappush(heap, (arr[i][0], i, 0))

    while heap:
        value, row, col = heapq.heappop(heap)
        result.append(value)

        if col + 1 < len(arr[row]):
            heapq.heappush(heap, (arr[row][col + 1], row, col + 1))

    return result

def main():
    arr = [[1, 2, 3, 4], [2, 2, 3, 4], [5, 5, 6, 6], [7, 8, 9, 9]]
    ans = mergeKSortedArray(arr)
    print(ans)

if __name__ == "__main__":
    main()
