usernames = input().split(", ")

for idx, username in enumerate(usernames):
    is_valid = True

    if not 3 <= len(username) <= 16:
        is_valid = False

    for char in username:
        if not char.isalnum() and char not in "-_":
            is_valid = False
            break

    if not is_valid:
        usernames[idx] = ""

usernames = [username for username in usernames if username]
print("\n".join(usernames))
