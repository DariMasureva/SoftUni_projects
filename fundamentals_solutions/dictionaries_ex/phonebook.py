phonebook = {}
search_count = 0
while True:
    command = input()
    if command.isdigit():
        search_count = int(command)
        break

    name, number = command.split("-")
    phonebook[name] = number

for _ in range(search_count):
    cur_name = input()
    cur_phone = phonebook.get(cur_name, f"Contact {cur_name} does not exist.")
    if cur_name in phonebook:
        print(f"{cur_name} -> {cur_phone}")
    else:
        print(cur_phone)
