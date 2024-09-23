
def ones_repeating(arr : list[int]):
    dict = {}
    
    for i in range(len(arr)):
        if arr[i] in dict:
            dict[arr[i]] += 1
        
        else:
            dict[arr[i]] = 1
    
    for key,value in dict.items():
        if value == 1:
            return key
        
def one_repeating(arr : list[int]):
    xorr = 0
    
    for i in arr:
        xorr ^= i 
    
    return xorr        
        
def main():
    arr = [4,1,2,1,2]
    lst = one_repeating(arr)
    print(lst)

if __name__ == "__main__":
    main()