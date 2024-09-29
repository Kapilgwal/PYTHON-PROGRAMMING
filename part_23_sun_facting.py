def sunFacing(arr : list[int]) -> int:
    temp = arr[0]
    cnt = 1
    for i in range(1,len(arr)):
        if arr[i] > temp:
            cnt += 1
            temp = arr[i]
    
    return cnt
            

def main():
    arr = [2,3,4,5]
    print(sunFacing(arr))
    
if __name__ == "__main__":
    main()