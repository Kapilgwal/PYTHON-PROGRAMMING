def rearrange(arr : list[int]) -> list[int]:
    pos = []
    neg = []
    
    for i in arr:
        if i > 0:
            pos.append(i)
        
        else:
            neg.append(i)
    
    for i in range(len(pos)):
        arr[2*i] = pos[i]
    
    for i in range(len(neg)):
        arr[2*i+1] = neg[i]
    
    return arr 

def main():
    arr = [1,2,-4,-5]
    ans = rearrange(arr)
    print(arr)

if __name__ == "__main__":
    main()