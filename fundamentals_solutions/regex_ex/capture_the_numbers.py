import re

numbers_found = []
regex = r"\d+"
while line := input():
    cur_numbers_found = re.findall(regex, line)
    if cur_numbers_found:
        numbers_found.extend(cur_numbers_found)

print(" ".join(numbers_found))
