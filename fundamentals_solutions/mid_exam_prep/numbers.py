initial_number_list = list(map(int, input().split()))
average_of_list = sum(initial_number_list) / len(initial_number_list)
greater_than_avrg = sorted([num for num in initial_number_list if num > average_of_list], reverse=True)
greater_than_avrg = list(map(str, greater_than_avrg[:5]))

if not greater_than_avrg:
    print("No")
else:
    print(" ".join(greater_than_avrg))
