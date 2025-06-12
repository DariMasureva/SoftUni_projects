initial_input = input().split()
command = input()

while command != "3:1":
    command = command.split()
    length = len(initial_input)

    if command[0] == "merge":
        start_idx = int(command[1])
        end_idx = int(command[2])

        if start_idx > length - 1:
            command = input()
            continue
        elif start_idx < - length:
            start_idx = - length

        if end_idx > length - 1:
            end_idx = length - 1
        elif end_idx < - length:
            command = input()
            continue

        merged = "".join(initial_input[start_idx:end_idx + 1])
        del initial_input[start_idx:end_idx + 1]
        initial_input.insert(start_idx, merged)

    elif command[0] == "divide":
        partit_idx = int(command[1])
        substr_count = int(command[2])
        element_divided = initial_input.pop(partit_idx)
        division_length = len(element_divided) // substr_count

        for substr_num in range(substr_count):

            if substr_num == substr_count - 1:
                cur_partit = element_divided
            else:
                cur_partit = element_divided[:division_length]

            element_divided = element_divided[division_length:]

            initial_input.insert(partit_idx + substr_num, cur_partit)

    command = input()

print(" ".join(initial_input))
