str = "geeksforgeeks"

dict = {}

for i in str:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
        
for i in str:
    if dict[i] == 1:
        print(i)