def getMinOpr(str1 : str,str2 : str,i : int,j : int,n : int,m : int) -> int:
    if i == n and j == m:
        return 0
    
    if i == n:
        return m - j
    if j == m:
        return n - i
    
    if str1[i] == str2[j]:
        return getMinOpr(str1,str2,i+1,j+1,n,m)
    
    else:
        return 1 + min(getMinOpr(str1,str2,i+1,j,n,m),getMinOpr(str1,str2,i,j+1,n,m))


def getMinimumInsertion(str1 : str,str2 : str) -> int:
    n = len(str1)
    m = len(str2)
    
    i = 0
    j = 0
    ans = getMinOpr(str1,str2,i,j,n,m)
    return ans

def main():
    str1 = "kapil"
    str2 = "malik"
    ans = getMinimumInsertion(str1,str2)
    print(ans)

if __name__ == "__main__":
    main()