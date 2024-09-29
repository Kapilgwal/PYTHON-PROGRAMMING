def countElement(arr : list[int]) -> list[int]:
    ans = []
    n = len(arr)
    
    for i in range(n):
        cnt = 0
        for j in range(i+1,n):
            if arr[i] > arr[j]:
                cnt += 1
        ans.append(cnt)
    return ans

def main():
    arr = [1,2,3,4,5]
    ans = countElement(arr)
    print(ans)
    
if __name__ == "__main__":
    main()