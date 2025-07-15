alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
total_sum = 0
commands = [command.strip() for command in input().split()]

for command in commands:
    start_letter = command[0]
    stop_letter = command[-1]
    number = int(command[1:-1])
    start_idx = alphabet.index(start_letter.lower()) + 1
    stop_idx = alphabet.index(stop_letter.lower()) + 1

    if start_letter.isupper():
        number /= start_idx
    else:
        number *= start_idx

    if stop_letter.isupper():
        number -= stop_idx
    else:
        number += stop_idx

    total_sum += number

print(f"{total_sum:.2f}")
