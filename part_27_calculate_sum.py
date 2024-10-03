str = "geeks4geeks"

sum = 0
temp = 0
for i in str:
    if i >= '0' and i<='9':
        temp = temp * 10 + int(i)
    
    else:
        sum += temp 
        temp = 0

sum += temp 
print(sum)
