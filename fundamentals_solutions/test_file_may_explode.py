initial_circle = input().split()
skip_count = int(input()) - 1
execution_list = []
list_length = len(initial_circle)
idx = skip_count

while initial_circle:

    while idx >= list_length and initial_circle:
        idx -= list_length

    execution_list.append(initial_circle[idx])
    initial_circle.remove(initial_circle[idx])
    list_length = len(initial_circle)

    if idx + skip_count > list_length:
        elements_left = list_length - idx
        idx = skip_count - elements_left

    else:
        idx += skip_count

final_str = ",".join(execution_list)
my_list = list(map(int, final_str.split()))
print(my_list)
