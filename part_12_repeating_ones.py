def find_ones(arr):
    temp = []

    for i in arr:
        if i in temp:
            temp.remove(i)
        else:
            temp.append(i)
    return temp[0]


def find_ones_best(arr):
    xorr = 0
    for i in arr:
        xorr = xorr ^ i
    return xorr


def main():
    arr = [4, 1, 2, 4, 2]
    print(find_ones(arr))
    print(find_ones_best(arr))


if __name__ == "__main__":
    main()
