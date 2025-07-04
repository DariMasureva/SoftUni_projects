gift_list = input().split()

command = input()

while command != "No Money":
    command = command.split()

    if "OutOfStock" in command and (command[1] in gift_list):
        gift_list = [gift if gift != command[1] else None for gift in gift_list]

    elif "Required" in command and (-1 < int(command[2]) < len(gift_list)):
        gift_list[int(command[2])] = command[1]

    elif "JustInCase" in command:
        gift_list[-1] = command[1]

    command = input()

gift_list = [gift for gift in gift_list if gift is not None]

print(" ".join(gift_list))
