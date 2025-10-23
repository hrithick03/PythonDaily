def palindrome(s):
    temp=s
    l=list(s)
    rev=""
    for i in range(len(s)-1,-1,-1):
        rev=rev+s[i]
    if (rev==temp):
        print("palindrome")    
    else:
        print("not palindrome")
    return 0
palindrome("malayalam")