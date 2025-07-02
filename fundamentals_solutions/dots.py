def find_group(board:list, group_list, coords_checked_list):
    group_found = False
    
    #finding a random dot from which to start the group
    for row_idx, row in enumerate(board):
        for symbol_idx, symbol in enumerate(row):
            start_dot_coords = (row_idx, symbol_idx)

            if symbol == "." and start_dot_coords not in coords_checked_list:
                group_list.append([start_dot_coords])
                coords_checked_list.append(start_dot_coords)
                group_found = True
                break
        if group_found:
            break
          
    #if there is a new group start found, we have to find tha rest of the group      
    if group_found:
        for dot_coords in group_list[-1]:
            y = dot_coords[0]
            x = dot_coords[1]
            cur_valid_idxs = validate_surrounding_coords(board, x, y)
            potential_positions = [(y, x+1), (y, x-1), (y+1, x), (y-1, x)]
            
            for idxs in cur_valid_idxs:
                cur_pos = potential_positions[idxs]

                if board[cur_pos[0]][cur_pos[1]] == "." and cur_pos not in coords_checked_list:
                    group_list[-1].append(cur_pos)
                    coords_checked_list.append(cur_pos)
                
    return group_list, coords_checked_list, group_found
                

def validate_surrounding_coords(board, x, y):
    values = [x+1, x-1, y+1, y-1]
    valid_idxs = []

    #determining if the positions around the current one are valid
    #valid_idxs = [index for index, value in enumerate(values) if 0 <= value < len(board[0])]
    for idx, value in enumerate(values):
        if (idx == 0 or idx == 1) and 0 <= value < len(board[0]):
            valid_idxs.append(idx)
        elif (idx == 2 or idx == 3) and 0 <= value < len(board):
            valid_idxs.append(idx)


    return valid_idxs

def find_biggest_group(group_list):
    return len(max(group_list, key=len))


rows = int(input())
field = [input().split() for _ in range(rows)]
coords_checked = []
groups = []

while True:
    groups, coords_checked, is_group_found = find_group(field, groups, coords_checked)
    if not is_group_found:
        break

biggest_group = find_biggest_group(groups)
print(biggest_group)
