text = input()
text_1 = text.replace(",", "")
text_2 = text_1.replace(".", "")
text_3 = text_2.replace("!", "")
text_4 = text_3.replace("?", "")
print(text_4.lower())
