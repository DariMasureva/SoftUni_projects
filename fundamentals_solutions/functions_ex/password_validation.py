import string


def password_validate(user_try: str):
    is_valid = True
    length = len(user_try)
    special_characters = string.punctuation
    digits = [symbol for symbol in user_try if symbol.isdigit()]
    comments = []

    if 6 > length or length > 10:
        comments.append("Password must be between 6 and 10 characters")
        is_valid = False

    for char in special_characters:
        if char in user_try:
            comments.append("Password must consist only of letters and digits")
            is_valid = False
            break

    if len(digits) < 2:
        comments.append("Password must have at least 2 digits")
        is_valid = False

    if is_valid:
        comments.append("Password is valid")

    return comments


user_input = input()
messages = password_validate(user_input)
for message in messages:
    print(message)
