def repeatingMissing(arr : list[int]):
    n = len(arr)
    repeating = 0
    missing = 0
    for i in range(1,n+1):
        cnt = 0
        for j in arr:
            if i==j:
                cnt += 1
        
        if cnt == 2:
            repeating = i
        
        if cnt == 0:
            missing = i 
    
    return repeating,missing

def repeatingMissingBetter(arr : list[int]):
    n = len(arr)
    repeating = 0
    missing = 0
    
    dict = {}
    
        
    for i in arr:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
            
    for i in range(1,n+1):
        if i in dict:
            if dict[i] == 2:
                 repeating = i
        else:
            missing = i  
    
    return repeating,missing

def repeatingMissingBetter2(arr : list[int]):
    n = len(arr)

    # Calculate the sum of first n natural numbers and the sum of squares
    sum_n = n * (n + 1) // 2
    sum_sq_n = n * (n + 1) * (2 * n + 1) // 6

    # Calculate the sum of array elements and the sum of squares of array elements
    sum_arr = sum(arr)
    sum_sq_arr = sum(x * x for x in arr)

    # Calculate the differences
    diff_sum = sum_n - sum_arr            # x - y
    diff_sq_sum = sum_sq_n - sum_sq_arr    # x^2 - y^2

    # From the equations, derive x + y = diff_sq_sum / diff_sum
    sum_xy = diff_sq_sum // diff_sum

    # Now we have:
    # x - y = diff_sum
    # x + y = sum_xy

    # Solving these two equations to find x and y
    missing = (diff_sum + sum_xy) // 2
    repeating = sum_xy - missing

    return repeating, missing

def main():
    arr = [3,1,2,5,3]
    # repeating,missing = repeatingMissing(arr)
    repeating,missing = repeatingMissingBetter2(arr)
    print(repeating,missing)
    
if __name__ == "__main__":
    main()