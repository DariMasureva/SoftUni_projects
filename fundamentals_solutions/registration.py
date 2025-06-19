def change_case(username, lower_or_upper):
    if lower_or_upper == "Lower":
        username = username.lower()
    else:
        username = username.upper()
    return username


def reverse(username, start, stop):
    substr = username[start:stop + 1]
    substr = substr[::-1]
    return substr


def cut_substring(username, substr):
    username = username.replace(substr, "")
    return username


def replace(username, char):
    username = username.replace(char, "-")
    return username


def validate(username, char):
    if char in username:
        return "Valid username."
    else:
        return f"{char} must be contained in your username."


initial_username = input()
result = ""

while True:
    command = input().split()
    action = command[0]

    if action == "Registration":
        break

    elif action == "Letters":
        lower_upper = command[1]
        initial_username = change_case(initial_username, lower_upper)
        result = initial_username

    elif action == "Reverse":
        start_idx = int(command[1])
        stop_idx = int(command[2])

        if 0 <= start_idx < len(initial_username) and 0 <= stop_idx < len(initial_username):
            result = reverse(initial_username, start_idx, stop_idx)
        else:
            continue

    elif action == "Substring":
        substring = command[1]

        if substring in initial_username:
            result = cut_substring(initial_username, substring)
            initial_username = result
        else:
            result = f"The username {initial_username} doesn't contain {substring}."

    elif action == "Replace":
        to_be_replaced = command[1]
        result = replace(initial_username, to_be_replaced)
        initial_username = result

    elif action == "IsValid":
        to_be_validated = command[1]
        result = validate(initial_username, to_be_validated)

    print(result)
