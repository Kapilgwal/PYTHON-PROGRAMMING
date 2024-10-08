def nCr(n,r):
    res = 1
    for i in range(r):
        res = res * (n-i)
        res = res // (i+1)
    return int(res)

def pascalTriangle(row : int) -> list[list[int]]:
    ans = []
    
    for row in range(1,row+1):
        tempLst = []
        for col in range(1,row+1):
            tempLst.append(nCr(row-1,col-1))
        ans.append(tempLst)
    return ans

def main():
    row = 6
    col = 3
    arr = pascalTriangle(row)
    print(arr)

if __name__ == "__main__":
    main()