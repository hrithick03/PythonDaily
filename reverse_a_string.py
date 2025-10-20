def reverse_str(s):
    reversed=[]
    for i in range(len(s)-1,-1,-1):
        reversed.append(s[i])
    return "".join(reversed)
print(reverse_str("hrithick"))

