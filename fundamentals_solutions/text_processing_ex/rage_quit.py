initial_rage = input()
non_numeric_chars = [char.lower() for char in initial_rage if not char.isdigit()]
unique_chars = set(non_numeric_chars)

cur_start_idx = 0
cur_iters = ""
cur_str = ""
final_rage = ""
number_found = False

for idx, char in enumerate(initial_rage):

    if idx == len(initial_rage) - 1:
        cur_iters += char
        final_rage += int(cur_iters) * cur_str.upper()

    elif number_found and not char.isdigit():
        number_found = False
        final_rage += int(cur_iters) * cur_str.upper()
        cur_iters = ""
        cur_str = char

    elif not char.isdigit():
        cur_str += char

    else:
        number_found = True
        cur_iters += char

print(f"Unique symbols used: {len(unique_chars)}")
print(final_rage)
