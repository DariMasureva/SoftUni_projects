first_str = input()
second_str = input()
current_list = list(first_str)
first_idx = 0

for first_ch in first_str:
    second_idx = 0

    for second_ch in second_str:
        if first_idx == second_idx:
            if first_ch == second_ch:
                second_idx += 1
                continue

            current_list[first_idx] = second_ch
            curr_str = "".join(current_list)
            print(curr_str)

        elif second_idx > first_idx:
            break

        second_idx += 1

    first_idx += 1
