def nonCons(temp : list[str]):
    
    for i in range(len(temp)-1):
        if temp[i] =='1' and temp[i+1] == '1':
            return False
    
    return True

def solve(temp : list[str],idx : int,ans : list[str]):
    if idx >= len(temp):
        if nonCons(temp):
            ans.append("".join(temp))
        return 
    
    solve(temp,idx+1,ans)
    
    if temp[idx] == '0':
        temp[idx] = '1'
        solve(temp,idx+1,ans)
        temp[idx] = '0'

def generateStrings(k : int):
    
    temp = ['0'] * k
    idx = 0
    ans = []
    solve(temp,idx,ans)
    
    return ans

def main():
    K = 3  
    ans = generateStrings(K)
    print(ans)
# Output : 000 , 001 , 010 , 100 , 101 
# Input : K  = 4 
# Output :0000 0001 0010 0100 0101 1000 1001 1010

if __name__ == "__main__":
    main()