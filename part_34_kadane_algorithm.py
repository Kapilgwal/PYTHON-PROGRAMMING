def kadaneAlgorithm(arr : list[int]) -> int:
    maxSum = -1e9
    n = len(arr)
    
    for i in range(n):
        for j in range(i,n):
            sum = 0
            for k in range(i,j+1):
                sum += arr[k]
            maxSum = max(maxSum,sum)
    
    return maxSum

def kadaneAlgorithmBetter(arr : list[int]) -> int:
    maxSum = -1e9
    n = len(arr)
    
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += arr[j]
            maxSum = max(maxSum,sum)
    
    return maxSum

def kadaneAlgorithmBest(arr : list[int]) -> int:
    maxSum = -1e9
    n = len(arr)
    
    sum = 0
    for i in range(n):
        sum += arr[i]
        maxSum = max(sum,maxSum)
        if sum < 0:
            sum = 0
    
    return maxSum        

def printKadane(arr : list[int]) -> list[int]:
    
    maxSum = -1e9
    sum = 0
    start = 0
    ansStart = -1
    ansEnd = -1
    
    for i in range(len(arr)):
        
        if sum == 0:
            start = i
        
        sum += arr[i]
        if sum > maxSum:
            maxSum = max(maxSum,sum)
            ansStart = start 
            ansEnd = i
        
        if sum < 0:
            sum = 0  
    
    
    ans = []
    for i in range(ansStart,ansEnd+1):
        ans.append(arr[i])
    
    return ans

def main():
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    print(kadaneAlgorithm(arr),kadaneAlgorithmBetter(arr),kadaneAlgorithmBest(arr),printKadane(arr))

if __name__ == "__main__":
    main()