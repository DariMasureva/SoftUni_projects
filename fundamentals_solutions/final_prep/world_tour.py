destinations = input()

while (command := input()) != "Travel":
    command_parts = command.split(":")
    action = command_parts[0]
    match action:
        case "Add Stop":
            idx, stop = command_parts[1:]
            idx = int(idx)
            if idx in range(len(destinations)):
                destinations = destinations[:idx] + stop + destinations[idx:]
        case "Remove Stop":
            start_idx, end_idx = map(int, command_parts[1:])
            if start_idx in range(len(destinations)) and end_idx in range(len(destinations)):
                destinations = destinations[:start_idx] + destinations[end_idx+1:]
        case "Switch":
            substr, replacement = command_parts[1:]
            if substr in destinations:
                destinations = destinations.replace(substr, replacement)
    print(destinations)

print(f"Ready for world tour! Planned stops: {destinations}")
