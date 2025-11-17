my_list = [1, 2, 2, 3, 4, 4, 4, 5]
freq = {}
for item in my_list:
    freq[item] = freq.get(item, 0) + 1
print(freq)
