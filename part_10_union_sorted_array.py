def union_array(arr1, arr2) -> list[int]:
    arr = []

    dict = {}

    for i in arr1:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    for i in arr2:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    for key, value in dict.items():
        arr.append(key)

    return arr


def union_array_best(arr1, arr2) -> list[int]:
    arr = []

    i = 0
    j = 0
    n = len(arr1)
    m = len(arr2)

    while i < n and j < m:

        if arr1[i] == arr2[j]:
            arr.append(arr1[i])
            i += 1
            j += 1

        elif arr1[i] < arr2[j]:
            if arr1[i] not in arr:
                arr.append(arr1[i])
            i += 1
        
        else:
            if arr2[j] not in arr:
                arr.append(arr2[j])
            j += 1

    while i < n:
        if arr1[i] in arr:
            i += 1

        if arr1[i] not in arr:
            arr.append(arr1[i])
            i += 1

    while j < m:
        if arr2[j] in arr:
            j += 1

        if arr2[j] not in arr:
            arr.append(arr2[j])
            j += 1
    
    return arr

def main():
    arr1 = [1, 2, 3, 4, 4, 5, 6, 6, 7]
    arr2 = [1, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 8, 9, 11]

    lst1 = union_array_best(arr1, arr2)
    lst2 = union_array_best(arr1, arr2)
    print(lst1)
    print(lst2)


if __name__ == "__main__":
    main()
