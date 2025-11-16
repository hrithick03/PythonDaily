def count_vowels_and_consonants(s):
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    v = 0
    c = 0
    i = 0
    while i < len(s):
        ch = s[i]
        if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
            ch_lower = ch.lower()

            is_vowel = False
            j = 0
            while j < len(vowels_list):
                if ch_lower == vowels_list[j]:
                    is_vowel = True
                    break
                j += 1

            if is_vowel:
                v += 1
            else:
                c += 1
        i += 1

    return v, c


text = input("Enter text: ")
vowels, consonants = count_vowels_and_consonants(text)
print("Vowels:", vowels, "Consonants:", consonants)
