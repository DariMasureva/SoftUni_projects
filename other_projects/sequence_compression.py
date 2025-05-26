sequence = list(input())
length = len(sequence)
compressed = []
counter = 0

if length == 0:
    print("The list is empty!!!")
elif length == 1:
    print(f"The only content of the list is {sequence[0]}")
else:
    current_symbol = sequence[0]

    for symbol in sequence:
        if symbol == current_symbol:
            counter += 1
        else:
            compressed.append((current_symbol, counter))
            counter = 1
            current_symbol = symbol
    else:
        compressed.append((current_symbol, counter))

    print(compressed)
