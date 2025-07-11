initial_string = input()
numbers = ""
letters = ""
other_symbols = ""

for char in initial_string:
    if char.isdigit():
        numbers += char
    elif char.isalpha():
        letters += char
    else:
        other_symbols += char

print(f"{numbers}\n{letters}\n{other_symbols}")
