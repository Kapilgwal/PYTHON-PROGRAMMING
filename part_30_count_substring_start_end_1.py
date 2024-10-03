str = "1001"

cnt = 0
for i in range(len(str)):
    temp = ""
    for j in range(i,len(str)):
        temp += str[j]
        
        if temp[0] == '1' and temp[-1] == '1' and len(temp) > 1:
            cnt+=1

print(cnt)

cnt2 = 0

for i in str:
    if i=='1':
        cnt2 += 1
    
print((cnt2*(cnt2-1))//2)