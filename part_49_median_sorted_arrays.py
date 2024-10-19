from collections import Counter

def frequency(arr : list[int]):
    return Counter(arr)

arr = [1,2,3,4,6,4,7,454,3,2,7,2,6,8,4,2,11,4,6,4,3]
temp = frequency(arr)
print(type(temp))