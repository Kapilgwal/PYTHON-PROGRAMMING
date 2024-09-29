def sortByFreq(arr : list[int]) -> list[int]:
    ans = []
    
    mydict = {}
    for i in arr:
        if i in mydict:
            mydict[i] += 1
        else:
            mydict[i] = 1
    
    sort = dict(sorted(mydict.items(), key = lambda item : item[1]))
    
    for key , value in sort.items():
        
        while value > 0:
            ans.append(key)
            value -= 1
    
    ans.reverse()
    return ans

def main():
    arr = [2,5,2,8,5,6,8,8]
    ans = sortByFreq(arr)
    print(ans)
    
if __name__ == "__main__":
    main()