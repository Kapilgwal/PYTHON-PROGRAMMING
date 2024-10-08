def rotate(arr : list[list[int]]) -> list[list[int]]:
    temp = [[0 for _ in range(len(arr))] for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr)):
            temp[j][len(arr) - i - 1] = arr[i][j]
    return temp

def rotatedBest(arr : list[list[int]]) -> list[list[int]]:
    n = len(arr)
    for i in range(n):
        for j in range(i,n):
            arr[i][j] , arr[j][i] = arr[j][i] , arr[i][j] 
    
    for i in range(n):
        arr[i].reverse()
    
    return arr

def printArr(arr : list[list[int]]):
    
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j],end=" ")
        print()
    print()
    
    
def main():
    arr = [[1,2,3],[4,5,6],[7,8,9]]
    printArr(arr)
    temp = rotatedBest(arr)
    printArr(temp)
    
if __name__ == "__main__":
    main()