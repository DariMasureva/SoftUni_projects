initial_input = list(input())
count_dict = {}

for char in initial_input:
    if char != " ":
        count_dict[char] = count_dict.get(char, 0) + 1

for char, count in count_dict.items():
    print(f"{char} -> {count}")
