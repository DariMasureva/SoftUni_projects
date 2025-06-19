initial_number_list = list(map(int, input().split()))


def swap(number_list, idx1, idx2):
    number_list[idx1], number_list[idx2] = number_list[idx2], number_list[idx1]
    return number_list


def multiply(number_list, idx1, idx2):
    number_list[idx1] = number_list[idx1] * number_list[idx2]
    return number_list


def decrease(number_list):
    number_list = [number - 1 for number in number_list]
    return number_list


while True:
    command = input()

    if command == "end":
        break

    command = command.split()
    action = command[0]

    if action == "swap":
        initial_number_list = swap(initial_number_list, int(command[1]), int(command[2]))
    elif action == "multiply":
        initial_number_list = multiply(initial_number_list, int(command[1]), int(command[2]))
    elif action == "decrease":
        initial_number_list = decrease(initial_number_list)

initial_number_list = [str(number) for number in initial_number_list]
print(", ".join(initial_number_list))
