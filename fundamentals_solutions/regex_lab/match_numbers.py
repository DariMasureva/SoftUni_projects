import re
initial_input = input()
pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
numbers = re.finditer(pattern, initial_input)
for number in numbers:
    print(number.group(), end=" ")
