from typing import List


def insertion_sort(lst: List[int]) -> List[int]:
    n = len(lst)
    for i in range(1, n):
        j = i
        while j > 0 and lst[j - 1] > lst[j]:

            lst[j], lst[j - 1] = lst[j - 1], lst[j]
            j -= 1

    return lst


def main():
    lst = [3, 2, 6, 4, 7, 8, 5]
    print(lst)
    lst = insertion_sort(lst)
    print(lst)


if __name__ == "__main__":
    main()
