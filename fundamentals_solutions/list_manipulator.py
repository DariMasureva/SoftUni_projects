list_of_numbers = [int(number) for number in input().split()]
odds = [number for number in list_of_numbers if number % 2 == 1]
evens = [number for number in list_of_numbers if number % 2 == 0]

command = input()

while command != "end":
    command = command.split()

    if command[0] == "exchange":
        split_idx = int(command[1])

        if split_idx > len(list_of_numbers) or split_idx < 0:
            print("Invalid index")
            command = input()
            continue

        first_half = list_of_numbers[:split_idx + 1]
        del list_of_numbers[:split_idx + 1]

        for number in first_half:
            list_of_numbers.append(number)

    elif command[0] == "max":

        if command[1] == "even" and evens:
            max_value = max(evens)
            max_value_count = evens.count(max_value)
        elif command[1] == "odd" and odds:
            max_value = max(odds)
            max_value_count = odds.count(max_value)
        else:
            print("No matches")
            command = input()
            continue

        if max_value_count > 1:
            max_idx = len(list_of_numbers) - list_of_numbers[::-1].index(max_value) - 1
        else:
            max_idx = list_of_numbers.index(max_value)

        print(max_idx)

    elif command[0] == "min":

        if command[1] == "even" and evens:
            min_value = min(evens)
            min_value_count = evens.count(min_value)
        elif command[1] == "odd" and odds:
            min_value = min(odds)
            min_value_count = odds.count(min_value)
        else:
            print("No matches")
            command = input()
            continue

        if min_value_count > 1:
            min_idx = len(list_of_numbers) - list_of_numbers[::-1].index(min_value) - 1
        else:
            min_idx = list_of_numbers.index(min_value)

        print(min_idx)

    elif command[0] == "first":
        odds = [number for number in list_of_numbers if number % 2 == 1]
        evens = [number for number in list_of_numbers if number % 2 == 0]
        firsts_count = int(command[1])
        even_len = len(evens)
        odd_len = len(odds)
        firsts = 0

        if firsts_count > len(list_of_numbers):
            print("Invalid count")
            command = input()
            continue

        elif command[2] == "even" and evens:
            if firsts_count <= even_len:
                firsts = evens[:firsts_count]
            else:
                firsts = evens

        elif command[2] == "odd" and odds:
            if firsts_count <= odd_len:
                firsts = odds[:firsts_count]
            else:
                firsts = odds

        elif command[2] == "odd" or command[2] == "even":
            print("[]")
            command = input()
            continue

        print(firsts)

    elif command[0] == "last":
        odds = [number for number in list_of_numbers if number % 2 == 1]
        evens = [number for number in list_of_numbers if number % 2 == 0]
        lasts_count = int(command[1])
        even_len = len(evens)
        odd_len = len(odds)
        lasts = 0

        if lasts_count > len(list_of_numbers):
            print("Invalid count")
            command = input()
            continue

        elif command[2] == "even" and evens:
            if lasts_count <= even_len:
                start_idx = even_len - lasts_count
                lasts = evens[start_idx:]
            else:
                lasts = evens

        elif command[2] == "odd" and odds:
            if lasts_count <= odd_len:
                start_idx = odd_len - lasts_count
                lasts = odds[start_idx:]
            else:
                lasts = odds

        elif command[2] == "odd" or command[2] == "even":
            print("[]")
            command = input()
            continue

        print(lasts)

    command = input()

print(list_of_numbers)
