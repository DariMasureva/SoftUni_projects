start_value = ord(input())
stop_value = ord(input())
text = input()
total_ascii_sum = 0

for char in text:
    if start_value < ord(char) < stop_value:
        total_ascii_sum += ord(char)

print(total_ascii_sum)
