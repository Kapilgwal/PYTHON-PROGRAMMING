# Corrected Code
input_str = "bAwutndekWEdkd"  # Initialize the input string (can modify this as needed)
lower = []  # List to store lowercase letters
upper = []  # List to store uppercase letters

# Separate characters into lowercase and uppercase lists
for char in input_str:
    if 'A' <= char <= 'Z':  # Check if character is uppercase
        upper.append(char)
    else:
        lower.append(char)

# Sort both lists
lower.sort()
upper.sort()

# Length of lowercase and uppercase lists
n1 = len(lower)
n2 = len(upper)

# New list to store the result
result = []

# Merge characters by alternating between upper and lower
i, j = 0, 0  # Pointers for lower and upper lists
while i < n1 and j < n2:
    if len(result) % 2 == 0:  # Even index -> add uppercase
        result.append(upper[j])
        j += 1
    else:  # Odd index -> add lowercase
        result.append(lower[i])
        i += 1

# If remaining lowercase characters exist, add them
while i < n1:
    result.append(lower[i])
    i += 1

# If remaining uppercase characters exist, add them
while j < n2:
    result.append(upper[j])
    j += 1

# Convert the list back to a string
output_str = "".join(result)
print(output_str)
