def getBinary(num):
    # Handle the case where num is 0
    if num == 0:
        return "0"
    
    string = ""
    while num > 0:
        rem = num % 2
        num = num // 2  # Use integer division
        string = str(rem) + string
    return string


def countFlip(start: int, goal: int):
    str1 = getBinary(start)
    str2 = getBinary(goal)

    count = 0
    
    # Pad the shorter string with leading zeros so both strings have equal length
    max_len = max(len(str1), len(str2))
    str1 = str1.zfill(max_len)
    str2 = str2.zfill(max_len)

    # Count the number of differing bits
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1

    return count


def main():
    start = 10
    goal = 7
    ans = countFlip(start, goal)
    print(ans)


if __name__ == "__main__":
    main()
