sequence = input().split()
initial_string_list = list(input())
message = ""

for number in sequence:
    digit_sum = 0

    for digit in number:
        digit_sum += int(digit)

    target_idx = digit_sum % len(initial_string_list)
    target_symbol = initial_string_list[target_idx]
    message += target_symbol
    initial_string_list.remove(initial_string_list[target_idx])


print(message)
