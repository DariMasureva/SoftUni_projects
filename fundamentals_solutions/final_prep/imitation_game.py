message = input()

while (command := input()) != "Decode":
    command_parts = command.split("|")
    action = command_parts[0]

    match action:
        case "Move":
            number_of_letters = int(command_parts[1])
            message = message[number_of_letters:] + message[:number_of_letters]

        case "Insert":
            idx, symbol = command_parts[1:]
            idx = int(idx)
            message = message[:idx] + symbol + message[idx:]

        case "ChangeAll":
            substr, replacement = command_parts[1:]
            message = message.replace(substr, replacement)

print(f"The decrypted message is: {message}")
