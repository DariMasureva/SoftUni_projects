message = input()

while (command := input()) != "Reveal":
    error_found = False
    command_parts = command.split(":|:")
    action = command_parts[0]

    match action:
        case "InsertSpace":
            idx = int(command_parts[1])
            message = message[:idx] + " " + message[idx:]
        case "Reverse":
            substr = command_parts[1]
            if substr in message:
                message = "{0}{1}".format(message.replace(substr, "", 1), substr[::-1])
            else:
                error_found = True
                print("error")
        case "ChangeAll":
            substr_to_be_replaced, replacement = command_parts[1:]
            message = message.replace(substr_to_be_replaced, replacement)

    if not error_found:
        print(message)

print(f"You have a new text message: {message}")
