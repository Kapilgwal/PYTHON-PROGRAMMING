# Function to count elements less than or equal to each
# element in arr1[]
 
def countElements(arr1, arr2, m, n):
    result = [0] * m
    frequency = [0] * 100010  # Hash table to store frequency of elements
 
    # Calculate frequency of elements in arr2
    for i in range(n):
        frequency[arr2[i]] += 1
 
    prefixSum = [0] * 100010
    prefixSum[0] = frequency[0]
 
    # Calculate prefix sum array
    for i in range(1, 100010):
        prefixSum[i] = prefixSum[i - 1] + frequency[i]
 
    # Count elements less than or equal to arr1[i]
    for i in range(m):
        result[i] = prefixSum[arr1[i]]
 
    # Print the counts
    for i in range(m):
        print(result[i], end=" ")
    print()
 
 
# Driver Code
if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 7, 9]
    arr2 = [0, 1, 2, 1, 1, 4]
    m = len(arr1)
    n = len(arr2)
    # Function Call
    countElements(arr1, arr2, m, n)