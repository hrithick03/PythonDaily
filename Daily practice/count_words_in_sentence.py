def count_words():
    s = input("Enter the string: ")
    count = 0
    in_word = False
    for char in s:
        if char != " ":
            if not in_word:
                count += 1
                in_word = True
        else:
            in_word = False
    return count
print(count_words())
