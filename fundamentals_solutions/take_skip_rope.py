def take_skip_repart(list_of_nums):
    even_idxs = []
    odd_idxs = []
    for idx, number in enumerate(list_of_nums):
        if idx % 2 == 0:
            even_idxs.append(number)
        else:
            odd_idxs.append(number)

    return even_idxs, odd_idxs


initial_input = list(input())
numbers_as_strings = "1234567890"
numbers_list = [int(number) for number in initial_input if number in numbers_as_strings]
other_symbols = [symbol for symbol in initial_input if symbol not in numbers_as_strings]
take_list, skip_list = take_skip_repart(numbers_list)
cur_idx = 0

for take_count, skip_count in zip(take_list, skip_list):
    start_skip_idx = cur_idx + take_count
    stop_skip_idx = start_skip_idx + skip_count
    del other_symbols[start_skip_idx:stop_skip_idx]

    cur_idx += take_count

if cur_idx != other_symbols[-1]:
    del other_symbols[cur_idx:]

print("".join(other_symbols))
