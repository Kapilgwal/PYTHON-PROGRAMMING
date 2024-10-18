def countWays(n: int) -> int:
    if n <= 1:
        return 1

    return countWays(n - 1) + countWays(n - 2)

def countWaysMem(n: int, dp : list[int]) -> int:
    if n <= 1:
        return 1
    
    if dp[n] != -1:
        return dp[n]

    dp[n] = countWays(n - 1) + countWays(n - 2)
    return dp[n]

def countWaysTab(n: int) -> int:
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
        
    return dp[n]

def countWaysOpm(n: int) -> int:
    dp = [0] * (n+1)
    prev2 = 1
    prev1 = 1
    
    for i in range(2,n+1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr 
        
    return prev1

def main():
    n = 5
    ans1 = countWays(n)
    dp = [-1] * (n+1)
    ans2 = countWaysMem(n,dp)
    ans3 = countWaysTab(n)
    ans4 = countWaysOpm(n)
    print(ans1,ans2,ans3,ans4)


if __name__ == "__main__":
    main()
