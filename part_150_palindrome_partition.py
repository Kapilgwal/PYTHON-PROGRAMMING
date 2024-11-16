def isPalindrome(s : str, start : int,end : int):
    while start <= end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

def solve(ans : list[list[str]], temp : list[str], index : int, s : str):
    if index >= len(s):
        ans.append(temp[:])
        return
    
    for i in range(index,len(s)):
        if isPalindrome(s,index,i):
            temp.append(s[index:i + 1])
            solve(ans,temp,i+1,s)
            temp.pop()
    

def palindromePartition(s : str):
    ans = []
    temp = []
    index = 0
    solve(ans,temp,index,s)
    return ans

def main():
    s = "aabb"
    ans = palindromePartition(s)
    print(ans)    

if __name__ == "__main__":
    main()