text = "Apple, banana! apple Orange; BANANA apple."
text = text.lower()
words = []
current_word = ""
for ch in text:
    if ch.isalpha():        
        current_word += ch
    else:
        if current_word:     
            words.append(current_word)
            current_word = ""
if current_word:
    words.append(current_word)
word_count = {}
for w in words:
    word_count[w] = word_count.get(w, 0) + 1
print(word_count)

