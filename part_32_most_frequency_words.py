arr = ['geeks', 'for', 'geeks', 'a', 'portal', 'to', 'learn', 'can', 'be',
       'computer', 'science', 'zoom', 'yup', 'fire', 'in', 'be', 'data', 'geeks']

mydict = {}

# Count the occurrences of each word in the array
for i in arr:
    if i in mydict:
        mydict[i] += 1
    else:
        mydict[i] = 1

# Sort the dictionary by values in ascending order
sorted_dict = dict(sorted(mydict.items(), key=lambda item: item[1]))

# Get the key with the highest frequency (last item in the sorted order)
most_frequent_word = list(sorted_dict.keys())[-1]

print(f"The most frequent word is: {most_frequent_word}")
