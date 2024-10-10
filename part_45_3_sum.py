def threeSum(arr : list[int],sum : int) -> list[list[int]]:
    n = len(arr)
    ans = []
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                total = arr[i] + arr[j] + arr[k]
                
                if sum == total:
                    temp = []
                    temp.append(arr[i])
                    temp.append(arr[j])
                    temp.append(arr[k])
                    temp.sort()
                    if temp not in ans:
                        ans.append(temp)
    
    return ans

def threeSumBetter(arr : list[int],sum : int) -> list[list[int]]:
    st = set()
    n = len(arr)
    for i in range(n):
        hashset = set()
        for j in range(i + 1, n):
            # Calculate the 3rd element:
            third = sum -(arr[i] + arr[j])

            # Find the element in the set:
            if third in hashset:
                temp = [arr[i], arr[j], third]
                temp.sort()
                st.add(tuple(temp))
            hashset.add(arr[j])

    # store the set in the answer:
    ans = list(st)
    return ans
                
def threeSumBest(arr : list[int], sum : int) -> list[list[int]]:
    ans = []
    arr.sort()
    n = len(arr)
    for i in range(n):
        # remove duplicates:
        if i != 0 and arr[i] == arr[i - 1]:
            continue

        # moving 2 pointers:
        j = i + 1
        k = n - 1
        while j < k:
            total_sum = arr[i] + arr[j] + arr[k]
            if total_sum < sum:
                j += 1
            elif total_sum > sum:
                k -= 1
            else:
                temp = [arr[i], arr[j], arr[k]]
                ans.append(temp)
                j += 1
                k -= 1
                # skip the duplicates:
                while j < k and arr[j] == arr[j - 1]:
                    j += 1
                while j < k and arr[k] == arr[k + 1]:
                    k -= 1

    return ans

def main():
    sum = 0
    arr = [-1,0,1,2,-1,-4]
    ans1 = threeSum(arr,sum)
    ans2 = threeSumBetter(arr,sum)
    ans3 = threeSumBest(arr,sum)
    print(ans1)
    print(ans2)
    print(ans3)
    
if __name__ == "__main__":
    main()