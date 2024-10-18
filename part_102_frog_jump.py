def solveRec(heights: list[int], index: int) -> int:
    if index == 0:
        return 0

    if index < 0:
        return 1e9

    left = abs(heights[index] - heights[index - 1]) + solveRec(heights, index - 1)

    right = 1e9
    if index > 1:
        right = abs(heights[index] - heights[index - 2]) + solveRec(heights, index - 2)

    return min(left, right)


def minEnergyRec(heights: list[int]) -> int:
    n = len(heights)
    ans = solveRec(heights, n - 1)
    return ans


def solveMem(heights: list[int], index: int, dp: list[int]) -> int:
    if index == 0:
        return 0

    if index < 0:
        return 1e9

    if dp[index] != -1:
        return dp[index]

    left = abs(heights[index] - heights[index - 1]) + solveMem(heights, index - 1, dp)

    right = 1e9
    if index > 1:
        right = abs(heights[index] - heights[index - 2]) + solveMem(
            heights, index - 2, dp
        )

    dp[index] = min(left, right)
    return dp[index]

def minEnergyMem(heights: list[int]) -> int:
    n = len(heights)
    dp = [-1 for _ in range(n + 1)]
    ans = solveMem(heights, n - 1, dp)
    return ans


def solveTab(heights: list[int]) -> int:
    n = len(heights)
    dp = [0 for _ in range(n+1)]
    dp[0] = 0
    
    for i in range(1,n):
        left = dp[i-1] + abs(heights[i] - heights[i-1])
        right = 1e9
        if i > 1:
            right = dp[i-2] + abs(heights[i] - heights[i-2])
        
        dp[i] = min(left,right)
    
    return dp[n-1]
        
def minEnergyTab(heights: list[int]) -> int:
    n = len(heights)
    ans = solveTab(heights)
    return ans

def main():
    heights = [10, 20, 30, 10]
    ans1 = minEnergyRec(heights)
    ans2 = minEnergyMem(heights)
    ans3 = minEnergyTab(heights)
    print(ans1,ans2,ans3)


if __name__ == "__main__":
    main()
