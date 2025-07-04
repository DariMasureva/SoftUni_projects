def coord_validity_check(board:list, x_pos, y_pos):
    x_values = [x_pos+1, x_pos-1]
    y_values = [y_pos+1, y_pos-1]

    #determining if the positions around the current one are valid
    validity = [True if 0 <= value < len(board[0]) else False for value in x_values]
    validity.extend([True if 0 <= value < len(board) else False for value in y_values])
    return validity

def path_continue(board:list, path_coords:list):
    for path in path_coords:
        for path_position in path:
            x = path_position[0]
            y = path_position[1]
            cur_validity  = coord_validity_check(board, x, y)
            potential_positions = [(y, x+1), (y, x-1), (y+1, x), (y-1, x)]

            for valid, cur_pos in zip(cur_validity, potential_positions):
                if valid and board[cur_pos[0]][cur_pos[1]] == " " and (cur_pos[1], cur_pos[0]) not in path:
                    path.append((cur_pos[1], cur_pos[0]))

    return path_coords

def start_paths(board:list, position:tuple):
    paths_found = []
    x = position[0]
    y = position[1]
    cur_validity = coord_validity_check(board, x, y)
    potential_positions = [(y, x + 1), (y, x - 1), (y + 1, x), (y - 1, x)]

    for valid, cur_pos in zip(cur_validity, potential_positions):
        if valid and board[cur_pos[0]][cur_pos[1]] == " ":
            paths_found.append([(cur_pos[1], cur_pos[0])])

    return paths_found

def find_kates_pos(board:list):
    kates_pos = (0,0)
    for idx, row in enumerate(board):
        if "k" in row:
            kates_pos = (row.index("k"), idx)
            break

    return kates_pos

def validate_paths(list_of_paths, board:list):
    valid_paths_list = []

    for cur_path in list_of_paths:
        x_ = cur_path[-1][0]
        y_ = cur_path[-1][1]

        if x_ == 0 or x_ == len(board[0]) - 1 or y_ == 0 or y_ == rows - 1:
            valid_paths_list.append(cur_path)

    return valid_paths_list


def find_longest_path(valid_paths_list):
    if not valid_paths_list:
        return "Kate cannot get out"
    else:
        longest_path = len(max(valid_paths_list, key=len)) + 1
        return f"Kate got out in {longest_path} moves"


#starting info
rows = int(input())
field = [input() for _ in range(rows)]

kates_position = find_kates_pos(field)
path_starts_ = start_paths(field, kates_position) #determining number of paths and the start coords
path_list = path_continue(field, path_starts_)
valid_paths = validate_paths(path_list, field)

print(find_longest_path(valid_paths))

