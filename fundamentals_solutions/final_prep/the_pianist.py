pieces_count = int(input())
pieces = {}

for _ in range(pieces_count):
    title, composer, key = input().split("|")
    pieces[title] = {"composer": composer, "key": key}

while (command := input()) != "Stop":
    info_parts = command.split("|")
    action = info_parts[0]

    match action:
        case "Add":
            piece, composer, key = info_parts[1:]
            if pieces.get(piece) is None:
                pieces[piece] = {"composer": composer, "key": key}
                print(f"{piece} by {composer} in {key} added to the collection!")
            else:
                print(f"{piece} is already in the collection!")

        case "Remove":
            piece = info_parts[1]
            if pieces.get(piece) is None:
                print(f"Invalid operation! {piece} does not exist in the collection.")
            else:
                pieces.pop(piece)
                print(f"Successfully removed {piece}!")

        case "ChangeKey":
            piece, new_key = info_parts[1:]
            if pieces.get(piece) is None:
                print(f"Invalid operation! {piece} does not exist in the collection.")
            else:
                pieces[piece]["key"] = new_key
                print(f"Changed the key of {piece} to {new_key}!")

for cur_piece, cur_piece_info in pieces.items():
    cur_composer, cur_key = cur_piece_info.values()
    print(f"{cur_piece} -> Composer: {cur_composer}, Key: {cur_key}")
