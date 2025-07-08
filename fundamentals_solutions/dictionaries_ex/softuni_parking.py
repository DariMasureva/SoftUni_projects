def register(username, license_number: str, parking: dict):
    if username not in parking.keys():
        parking[username] = license_number
        message = f"{username} registered {license_number} successfully"
    else:
        message = f"ERROR: already registered with plate number {parking[username]}"

    return message


def unregister(username: str, parking: dict):
    if username not in parking.keys():
        message = f"ERROR: user {username} not found"
    else:
        del parking[username]
        message = f"{username} unregistered successfully"

    return message


parking_lot = {}
command_count = int(input())

for _ in range(command_count):
    command = input().split()

    if command[0] == "register":
        name, plate_number = command[1::]
        result = register(name, plate_number, parking_lot)

    else:
        name = command[1]
        result = unregister(name, parking_lot)

    print(result)

for name, plate_number in parking_lot.items():
    print(f"{name} => {plate_number}")
