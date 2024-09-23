def find_missing(arr : list[int]):
    
    for i in range(1,len(arr) + 1):
        if i not in arr:
            return i

def missing_number(arr : list[int],n):
    sum1 = ((n)*(n+1))//2
    sum2 = 0
    for i in range(len(arr)):
        sum2 += arr[i]
    
    return sum1 - sum2

def main():
    arr = [1,2,4,5,6]
    print(missing_number(arr,6))
    
if __name__ == "__main__":
    main()