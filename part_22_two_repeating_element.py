# def repeatingElements(arr : list[int]) -> list[int]:
#     ans = []
    
#     xorr = 0
    
#     for i in arr:
#         xorr = xorr ^ i 
        
#         if xorr == 0:
#             ans.append(i)
    
#     return ans

def repeatingElements(arr: list[int]) -> list[int]:
    ans = []
    mydict = {}
    
    for i in arr:
        if i not in mydict:
            mydict[i] = 1
        else:
            mydict[i] += 1
    
    for key, value in mydict.items():
        if value > 1:
            ans.append(key)
    
    return ans
        

def main():
    arr = [4,2,4,5,2,3,1]
    ans = repeatingElements(arr)
    print(ans)

if __name__ == "__main__":
    main()