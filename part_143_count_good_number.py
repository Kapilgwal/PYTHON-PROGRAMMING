def is_good(num_str):
    for i in range(len(num_str)):
        digit = int(num_str[i])
        if i % 2 == 0:
            if digit % 2 != 0:
                return False
        else:
            if digit not in {2, 3, 5, 7}:
                return False
    return True

def goodNumbers(n: int) -> int:
    count = 0
    for i in range(0, pow(10, n)):
        if is_good(str(i)):
            count += 1

    return count

def main():
    n = 50
    ans = goodNumbers(n)
    print(ans)


if __name__ == "__main__":
    main()
