forces = {}

while (command:=input()) != "Lumpawaroo":

    if "|" in command:
        force, user = command.split(" | ")
        force_user_exists = False

        for user_list in forces.values():
            if user in user_list:
                force_user_exists = True
                break

        if not force_user_exists:

            if force not in forces:
                forces[force] = [user]
            else:
                forces[force].append(user)

    else:
        user, force = command.split(" -> ")

        for user_list in forces.values():
            if user in user_list:
                user_list.remove(user)
                break

        if force not in forces:
            forces[force] = [user]
        else:
            forces[force].append(user)

        print(f"{user} joins the {force} side!")

for force, user_list in forces.items():
    if user_list:
        print(f'Side: {force}, Members: {len(user_list)}')
        for user in user_list:
            print(f"! {user}")
