def move_zeros_end(arr : list[int]):
    cnt = 0
    
    for i in range(len(arr)):
        
        if arr[i] != 0:
            arr[cnt] = arr[i]
            cnt += 1
    
    for i in range(cnt,len(arr)):
        arr[i] = 0
        
def move_zeros_end_brute(arr : list[int]):
    temp = []
    cnt = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            cnt += 1
        else:
            temp.append(arr[i])
    print(temp)
    for i in range(len(temp)):
        arr[i] = temp[i]
        
    for i in range(len(temp),len(temp) + cnt):
        arr[i] = 0
        
def main():
    arr = [1,0,2,3,0,4,0,1]
    print(arr)
    move_zeros_end_brute(arr)
    print(arr)
    
if __name__ == "__main__":
    main()