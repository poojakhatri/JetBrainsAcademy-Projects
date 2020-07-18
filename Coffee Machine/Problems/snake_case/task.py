word = input()
for char in word:
    if char.isupper():
        word = word.replace(char, '_' + char.lower())
print(word)
