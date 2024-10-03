str1 = "geeks"
str2 = "forgeeks"

str = ""
i = 0
j = 0
n1 = len(str1)
n2 = len(str2)

while i<n1 and j<n2:
    if len(str)%2==0:
        str += (str1[i])
        i += 1
    else:
        str += (str2[j])
        j += 1
        
while i < n1:
    str += (str1[i])
    i += 1

while j < n2:
    str += (str2[j])
    j += 1
    
print(str)


n = 44

temp = n/10
rem = n%10 

if rem >= 5:
    temp = int(temp)
    temp = temp*10
    temp += 10

else:
    temp = int(temp)
    temp = temp*10 

print(temp)