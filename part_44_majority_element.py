def majorityElements(arr : list[int]):
    ans = []
    n = len(arr)
    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[i] == arr[j]:
                cnt += 1
        
        if cnt > n/3:
            if arr[i] not in ans:
                ans.append(arr[i])
    
    return ans

def majorityElementsBetter(arr : list[int]):
    
    dict = {}
    n = len(arr)
    
    for i in arr:
        if i in dict:
            dict[i] += 1
        
        else:
            dict[i] = 1
    ans = []
    
    for key,values in dict.items():
        if values > n/3:
            ans.append(key)
    
    return ans


def majorityElementsBest(v: list[int]) -> list[int]:
    n = len(v) 

    cnt1, cnt2 = 0, 0 
    el1, el2 = float('-inf'), float('-inf')

    for i in range(n):
        if cnt1 == 0 and el2 != v[i]:
            cnt1 = 1
            el1 = v[i]
        elif cnt2 == 0 and el1 != v[i]:
            cnt2 = 1
            el2 = v[i]
        elif v[i] == el1:
            cnt1 += 1
        elif v[i] == el2:
            cnt2 += 1
        else:
            cnt1 -= 1
            cnt2 -= 1

    ls = [] 
    cnt1, cnt2 = 0, 0
    for i in range(n):
        if v[i] == el1:
            cnt1 += 1
        if v[i] == el2:
            cnt2 += 1

    mini = int(n / 3) + 1
    if cnt1 >= mini:
        ls.append(el1)
    if cnt2 >= mini:
        ls.append(el2)

    return ls


def main():
    # arr = [1,2,2,3,2]
    arr = [11,33,33,11,33,11]
    ans1 = majorityElements(arr)
    ans2 = majorityElementsBetter(arr)
    ans3 = majorityElementsBest(arr)
    print(ans1,ans2,ans3)
    
if __name__ == "__main__":
    main()