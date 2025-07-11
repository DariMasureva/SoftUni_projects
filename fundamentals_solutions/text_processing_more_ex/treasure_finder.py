keys = list(map(int, input().split()))
key_idx = 0
treasure_info = ""

while (clue := input()) != 'find':
    treasure_info = ""

    for char in clue:
        if key_idx == len(keys):
            key_idx = 0

        new_char_ascii = ord(char) - keys[key_idx]
        treasure_info += chr(new_char_ascii)
        key_idx += 1

    start_treasure_type = treasure_info.index("&") + 1
    stop_treasure_type = treasure_info.index("&", start_treasure_type)
    treasure_type = treasure_info[start_treasure_type:stop_treasure_type]

    start_treasure_coords = treasure_info.index("<") + 1
    stop_treasure_coords = treasure_info.index(">")
    treasure_coords = treasure_info[start_treasure_coords:stop_treasure_coords]

    key_idx = 0

    print(f"Found {treasure_type} at {treasure_coords}")
