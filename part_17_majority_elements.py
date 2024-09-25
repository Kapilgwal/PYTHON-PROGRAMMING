def majorityElements(arr : list[int]) -> int:
    for i in range(len(arr)):
        cnt = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                cnt += 1
        
        if cnt > len(arr)/2:
            return arr[i]
            break   

def main():
    arr = [3,2,3]
    print(majorityElements(arr))
    
if __name__ == "__main__":
    main()