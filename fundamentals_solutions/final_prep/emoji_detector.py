import math
import re

text = input()
coolness_pattern = r"\d"
emoji_pattern = r"(::|\*\*)([A-Z][a-z]{2,})\1"

# finding all digits, putting them in a list and finding the product of the elements
digits_found = re.findall(coolness_pattern, text)
coolness_threshold = math.prod([int(digit) for digit in digits_found])
all_emojis = re.findall(emoji_pattern, text)
valid_emojis = []
for emoji in all_emojis:
    # we take group 1 of every emoji because it contains the actual text
    cur_coolness = sum(ord(symbol) for symbol in emoji[1])
    if cur_coolness >= coolness_threshold:
        valid_emojis.append(emoji)

print(f"Cool threshold: {coolness_threshold}")
print(f"{len(all_emojis)} emojis found in the text. The cool ones are:")
for emoji in valid_emojis:
    print(emoji[0]+emoji[1]+emoji[0])

