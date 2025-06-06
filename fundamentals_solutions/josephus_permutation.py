initial_circle = input().split()
skip_count = int(input()) - 1

execution_list = []
idx = skip_count

while initial_circle:
    list_length = len(initial_circle)

    # this is to make sure k is less than the list length at all times
    if idx >= list_length and initial_circle:
        idx %= list_length

    executed = initial_circle.pop(idx)
    execution_list.append(executed)

    idx += skip_count

formatted_execution_list = ",".join(execution_list)
print(f"[{formatted_execution_list}]")
