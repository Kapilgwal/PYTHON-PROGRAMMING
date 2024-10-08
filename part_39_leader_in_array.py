def leaderArray(arr : list[int]) -> int:
    ans = []
    
    for i in range(len(arr)):
        leader = True
        for j in range(i+1,len(arr)):
             if arr[j] > arr[i]:
                leader = False
                break
             
        if leader:
            ans.append(arr[i])
            
    return ans

def leaderArrayBetter(arr : list[int]) -> int:
    ans = []
    arr.reverse()
    ans.append(arr[0])
    maxi = arr[0]
    
    for i in range(1,len(arr)):
        
        if arr[i] > maxi:
            ans.append(arr[i])
            maxi = arr[i]
    
    return ans
    

def main():
    
    # arr = [10,22,12,3,0,6]
    arr = [4,7,1,0]
    ans1 = leaderArray(arr)
    ans2 = leaderArrayBetter(arr)
    print(ans1)
    
if __name__ == "__main__":
    main()