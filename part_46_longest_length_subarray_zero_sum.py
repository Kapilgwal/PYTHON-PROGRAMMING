def longestLengthBrute(arr : list[int]) -> int:
    n = len(arr)
    maxLen = 0
    for i in range(n):
        sum = 0
    
        for j in range(i,n):
            sum += arr[j]
            
            if sum == 0:
                maxLen = max(maxLen,j-i+1)
    
    return maxLen

def longestLengthBetter(arr : list[int]) -> int:
    n = len(arr)
    
    maxLen = 0
    preSum = {}
    preSum[0] = 0
    sum = 0
    for i in range(n):
        sum += arr[i]
        
        if sum == 0:
            maxLen = max(maxLen,i+1)
            
        else:
            if (sum) in preSum:
                maxLen = max(maxLen,i - preSum[sum])
        
            else:
                preSum[sum] = i
                
    return maxLen

def main():
    arr = [9,-3,3,-1,6,-5]
    ans1 = longestLengthBrute(arr)
    ans2 = longestLengthBetter(arr)
    print(ans1,ans2)
    
if __name__ == "__main__":
    main()