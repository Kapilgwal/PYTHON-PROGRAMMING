def AssignCookies(g : list[int], s : list[int]) -> int:
    n = len(g)
    m = len(s)
    g.sort()
    s.sort()
    
    l = 0
    r = 0
    # count = 0
    while l < m and r < n:
        
        if s[l] >= g[r]:
            r += 1
        l += 1
    
    return r

def main():
    g = [1,5,3,3,4]
    s = [4,2,1,2,1,3]
    ans = AssignCookies(g,s)
    print(ans) 

if __name__ == "__main__":
    main()