str = "00011"

left = 0
right = 0

for i in range(len(str)):
    if str[i] =='1':
        left = i
        break 

for i in reversed(range(len(str))):
    if str[i] == '1':
        right = i 
        break 
    
for i in range(left,right):
    if str[i] == '0':
        print("INVALID") 
        exit() 

print("VALID")

def to_upper_case(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            result += chr(ord(char) & ~32)
        else:
            result += char
    return result

# Driver code
strr = "SanjaYKannA"
print(to_upper_case(strr))
