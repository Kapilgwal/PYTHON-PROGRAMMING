def majorityElements(arr: list[int]) -> int:
    for i in range(len(arr)):
        cnt = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                cnt += 1

        if cnt > len(arr) / 2:
            return arr[i]
            break


def majorityElementsBetter(arr: list[int]) -> int:

    dict = {}
    for i in arr:
        if i not in dict:
            dict[i] = 1

        else:
            dict[i] += 1

    for key, value in dict.items():

        if value > len(arr) / 2:
            return key

    return -1


def majorityElementsBest(arr: list[int]) -> int:

    cnt = 1
    ele = arr[0]

    for i in range(1, len(arr)):

        if ele == arr[i]:
            cnt += 1

        elif cnt == 0:
            ele = arr[i]
            cnt = 1

        else:
            cnt -= 1

    for i in arr:

        if i == ele:
            cnt += 1

    if cnt > len(arr) / 2:
        return ele

def main():
    arr = [3, 2, 3, 2, 2, 2]
    print(majorityElements(arr))
    print(majorityElementsBetter(arr))
    print(majorityElementsBest(arr))


if __name__ == "__main__":
    main()
