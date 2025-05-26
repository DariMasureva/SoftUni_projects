pair_count = int(input())

pair_sums = []
diffs = []
first_of_pair = 0
second_of_pair = 0
max_diff = 0
diff_count = 0

for num in range(pair_count * 2):
    current_num = int(input())
    if num % 2 == 0:
        first_of_pair = current_num
    else:
        second_of_pair = current_num
        pair_sum = first_of_pair + second_of_pair
        pair_sums.append(pair_sum)

for i in range(pair_count - 1):
    diff = abs(pair_sums[i] - pair_sums[i + 1])
    if diff != 0:
        diffs.append(diff)
        diff_count += 1
    i += 1

if not diffs:
    print(f"Yes, value={pair_sums[0]}")
else:
    for i in range(diff_count):
        if diffs[i] > max_diff:
            max_diff = diffs[i]

    print(f"No, maxdiff={max_diff}")
