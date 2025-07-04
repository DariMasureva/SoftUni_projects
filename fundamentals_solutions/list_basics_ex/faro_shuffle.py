initial_list = input().split()
half_idx = int(len(initial_list)/2)
faro_count = int(input())
final_list = []

for current_faro in range(faro_count):
    first_half = initial_list[:half_idx]
    second_half = initial_list[half_idx:]

    for idx in range(len(first_half)):
        final_list.append(first_half[idx])
        final_list.append(second_half[idx])

    if current_faro != faro_count - 1:
        initial_list = final_list
        final_list = []

print(final_list)
