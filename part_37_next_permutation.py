def nextPermutation(arr : list[int]) -> int:
    ind = -1
    n = len(arr)
    for i in range(n-2,-1,-1):
        if arr[i] < arr[i+1]:
            ind = i
            break 
    
    if ind == -1:
        arr.reverse()
        return arr 
    
    for i in range(n-1,ind,-1):
        if arr[i] > arr[ind]:
            arr[i],arr[ind] = arr[ind],arr[i]
            break
    
    arr[ind+1:] = reversed(arr[ind+1:])
    
    return arr

def main():
    arr = [1,3,2]
    ans = nextPermutation(arr)
    print(ans)
    
if __name__ == "__main__":
    main()