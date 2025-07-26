activation_key = input()
case_types = {"Lower": lower(), }

while (command := input()) != "Generate":
    command_parts = command.split(">>>")
    action = command_parts[0]
    match action:
        case "Contains":
            substr = command_parts[1]
            if substr in activation_key:
                print(f"{activation_key} contains {substr}")
            else:
                print("Substring not found!")
        case "Flip":
            case_type = command_parts[1] #upper or lower
            start_idx, stop_idx = map(int, command_parts[2:])

        case "Slice":
            pass
