password = input()
while (command := input()) != "Done":
    command_parts = command.split()
    action = command_parts[0]
    change_denied = False

    match action:
        case "TakeOdd":
            password = password[1::2]
        case "Cut":
            idx, length = map(int, command_parts[1:])
            password = password[:idx] + password[idx+length:]
        case "Substitute":
            substr, replacement = command_parts[1:]
            if substr in password:
                password = password.replace(substr, replacement)
            else:
                change_denied = True
                print("Nothing to replace!")
    if not change_denied:
        print(password)

print(f"Your password is: {password}")
