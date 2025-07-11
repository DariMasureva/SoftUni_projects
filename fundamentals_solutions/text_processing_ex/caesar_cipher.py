message = list(input())

for idx, symbol in enumerate(message):
    new_ascii_val = ord(symbol) + 3
    new_symbol = chr(new_ascii_val)
    message[idx] = new_symbol

print("".join(message))
