def minSubsetDiff(arr : list[int],sum1 : int,index : int,n : int,sum2 : int):
    if index >= n:
        return 0
    
    take = minSubsetDiff(arr,sum1,index+1,n,sum2 + arr[index])
    notTake = minSubsetDiff(arr,sum1,index+1,n,sum2)
    
    return 

def main():
    arr = [1,2,3,4]
    sum1 = 0
    for it in arr:
        sum1 += it 
        
    ans = minSubsetDiff(arr,sum1,0,len(arr),0)
    print(sum1)
    
if __name__ =="__main__":
    main()
    