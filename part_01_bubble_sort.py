from typing import List


def bubble_sort(lst: List[int]) -> List[int]:
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):

            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

    return lst


def main():
    lst = [3, 2, 6, 4, 7, 8, 5]
    print(lst)
    lst = bubble_sort(lst)
    print(lst)


if __name__ == "__main__":
    main()
