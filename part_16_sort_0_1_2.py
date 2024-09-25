def sort_0_1_2(arr : list[int]):
    arr.sort()
    return arr

def sort_0_1_2_better(arr : list[int]):
    zero = 0
    one = 0
    two = 0
    
    for i in arr:
        if i == 0:
            zero += 1
        if i == 1:
            one += 1
        if i == 2:
            two += 1
    
    idx = 0
    while zero > 0:
        arr[idx] = 0
        zero -= 1
        idx += 1    
    
    while one > 0:
        arr[idx] = 1
        one -= 1
        idx += 1    
        
    while two > 0:
        arr[idx] = 2
        two -= 1
        idx += 1
        
    return arr

def sort_0_1_2_best(arr : list[int]):
    low = 0
    mid = 0
    high = len(arr) - 1
    
    while mid <= high:
        
        if arr[mid] == 0:
            arr[low],arr[mid] = arr[mid],arr[low]
            low += 1
            mid += 1
        
        elif arr[mid] == 1:
            mid += 1
        
        else:
            arr[high] , arr[mid] = arr[mid] , arr[high]
            high -= 1
            mid += 1 
    
    return arr
        
    
def main():
    arr = [2,0,2,1,1,0]
    print(arr)
    # arr1 = sort_0_1_2(arr)
    # arr2 = sort_0_1_2_better(arr)
    arr3 = sort_0_1_2_best(arr)
    # print(arr1)
    # print(arr2)
    print(arr3)
    
if __name__ == "__main__":
    main()