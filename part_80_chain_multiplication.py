from collections import deque


def chainMultiplication(arr: list[int], start: int, end: int) -> int:
    q = deque()
    q.append((start, 0))
    dist = [float("inf")] * 100000
    dist[start] = 0
    mod = 100000

    while q:
        num, steps = q.popleft()

        for i in arr:
            new_num = (num * i) % mod
            if steps + 1 < dist[new_num]:
                dist[new_num] = steps + 1
                if new_num == end:
                    return steps + 1
                q.append((new_num, steps + 1))

    return -1


def main():
    arr = [3, 4, 65]
    start = 7
    end = 66175
    ans = chainMultiplication(arr, start, end)
    print(ans)


if __name__ == "__main__":
    main()
