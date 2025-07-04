initial_number_list = list(map(int, input().split(", ")))
cur_stop = 10

while initial_number_list:
    cur_list = [number for number in initial_number_list if number <= cur_stop]
    initial_number_list = [number for number in initial_number_list if number not in cur_list]
    print(f"Group of {cur_stop}'s: {cur_list}")
    cur_stop += 10
