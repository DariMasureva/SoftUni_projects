import re

text = input()
word_searched = input()
regex = r"\b" + word_searched + r"\b"
word_occur_count = len(re.findall(regex, text, re.IGNORECASE))
print(word_occur_count)
