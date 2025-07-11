strings = input().split()
total_sum = 0
longer_str = strings[0] if len(strings[0]) > len(strings[1]) else strings[1]
shorter_str = strings[0] if longer_str == strings[1] else strings[1]

for idx in range(len(shorter_str)):
    total_sum += ord(shorter_str[idx]) * ord(longer_str[idx])

total_sum += sum(map(ord, longer_str[len(shorter_str)::]))
print(total_sum)
