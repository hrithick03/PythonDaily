def contains_substring(string, substring):
    str_len = len(string)
    sub_len = len(substring)
    for i in range(str_len - sub_len + 1):
        match = True
        for j in range(sub_len):
            if string[i + j] != substring[j]:
                match = False
                break
        if match:
            return True
    return False
string = "Hello world"
substring = "world"

if contains_substring(string, substring):
    print("Substring exists")
else:
    print("Substring not found")
