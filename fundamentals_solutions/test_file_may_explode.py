initial_message = input().split()

for word in initial_message:
    ascii_code = filter(lambda x: x.isdigit(), word)
