str1 = "occurrence"
str2 = "car"
str = []

for i in str2:
    str.append(i)

temp = ""
for i in str1:
    if i not in str:
        temp += i

print(temp)

strrr = "g ee kk sss f       ro  k"

tt = ""
for i in strrr:
    if i == ' ':
        continue 
    else:
        tt += i 
print(tt)

strrr = strrr.replace(' ','')
print(strrr)