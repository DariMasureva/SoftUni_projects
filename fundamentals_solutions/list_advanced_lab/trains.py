wagons_count = int(input())
train = [0 for _ in range(wagons_count)]
command = input()

while command != "End":
    command = command.split()

    if command[0] == "add":
        people_count = int(command[1])
        train[-1] += people_count

    elif command[0] == "insert":
        wagon_number = int(command[1])
        people_count = int(command[2])
        train[wagon_number] += people_count

    elif command[0] == "leave":
        wagon_number = int(command[1])
        people_count = int(command[2])
        train[wagon_number] -= people_count

    command = input()

print(train)
