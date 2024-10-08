import sys

def longestSequence(arr : list[int]) -> int:
    maxSeq = 0
    for i in range(len(arr)):
        seq = 1
        curr = arr[i]
        
        while (curr + 1) in arr:
            seq += 1
            curr += 1
        
        maxSeq = max(maxSeq,seq)
    return maxSeq      
    

def longestSequenceBetter(arr : list[int]) -> int:
    
    arr.sort()
    cnt= 1
    maxCnt = -sys.maxsize
    for i in range(len(arr)-1):
        
        if arr[i+1] == arr[i] + 1:
            cnt += 1
            maxCnt = max(maxCnt,cnt)
        
        else:
            cnt = 1
    
    return maxCnt

def longestSequenceBetter2(arr : list[int]) -> int:
    
    n = len(arr)
    
    if n==0:
        return 0
    
    st = set()
    
    for i in arr:
        st.add(i)
    
    longest = 1
    
    for it in st:
        
        if it -1 not in st:
            cnt = 1
            x = it
            
            while x + 1 in st:
                x += 1
                cnt += 1
            longest = max(longest,cnt)
            
    return longest
        
                          
def main():
    arr =  [100, 200,201,202,203,204,205,206, 1, 3, 2, 4,5]
    ans1 = longestSequence(arr)
    ans2 = longestSequenceBetter(arr)
    ans3 = longestSequenceBetter2(arr)
    print(ans1,ans2,ans3)
    
if __name__ == "__main__":
    main()