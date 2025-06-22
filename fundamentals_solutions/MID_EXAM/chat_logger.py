chat = []

while True:
    command = input().split()
    action = command[0]

    if action == "end":
        print(f"\n".join(chat))
        break

    elif action == "Chat":
        message = command[1]
        chat.append(message)

    elif action == "Delete":
        message = command[1]
        if message in chat:
            chat.remove(message)

    elif action == "Edit":
        message, edited_mess = command[1:]
        if message in chat:
            mess_idx = chat.index(message)
            chat[mess_idx] = edited_mess

    elif action == "Pin":
        message = command[1]
        if message in chat:
            chat.remove(message)
            chat.append(message)

    elif action == "Spam":
        messages = command[1:]
        chat.extend(messages)
