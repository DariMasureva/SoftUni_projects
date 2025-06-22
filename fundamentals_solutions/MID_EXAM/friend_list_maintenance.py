def blacklist_someone(fr_list, friend_name:str):
        fr_idx = fr_list.index(friend_name)
        fr_list[fr_idx] = "Blacklisted"
        return f"{friend_name} was blacklisted."


def error(fr_list, index, lost_count_):
    error_name = fr_list[index]

    if error_name != "Blacklisted" and error_name != "Lost":
        fr_list[index] = "Lost"
        lost_count_ += 1
        return f"{error_name} was lost due to an error.", lost_count_
    else:
        return "", lost_count_


def change_name(fr_list, index, changed_name):
    cur_name = fr_list[index]
    fr_list[index] = changed_name
    return f"{cur_name} changed his username to {changed_name}."


friend_list = input().split(", ")
blacklist = []
lost_count = 0

while True:
    message = ""
    command = input().split()
    action = command[0]
    if action == "Report":
        print(f"Blacklisted names: {len(blacklist)}")
        print(f"Lost names: {lost_count}")
        print(" ".join(friend_list))
        break

    if action == "Blacklist":
        name = command[1]
        if name in friend_list:
            blacklist.append(name)
            message = blacklist_someone(friend_list, name)
        else:
            message = f"{name} was not found."

    elif action == "Error":
        idx = int(command[1])
        if 0 <= idx < len(friend_list):
            message, lost_count = error(friend_list, idx, lost_count)

    elif action == "Change":
        idx, new_name = int(command[1]), command[2]
        if 0 <= idx < len(friend_list):
            message = change_name(friend_list, idx, new_name)

    if message:
        print(message)
