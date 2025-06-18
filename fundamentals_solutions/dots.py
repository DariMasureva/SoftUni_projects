def find_dot_positions(game_field):
    positions = []
    for row_idx, row in enumerate(game_field):
        for symb_idx, symb in enumerate(row.split(" ")):

            if symb == ".":
                positions.append((row_idx, symb_idx))

    return positions


def find_connections(dot_coords):
    connections_coords = {dot_coords[0]}

    for cur_y, cur_x in connections_coords:

        if ((int(cur_y) - 1), cur_x) in dots_positions:
            connections_coords.add(((int(cur_y) - 1), cur_x))
        if ((int(cur_y) + 1), cur_x) in dots_positions:
            connections_coords.add(((int(cur_y) + 1), cur_x))
        if (cur_y, (int(cur_x) - 1)) in dots_positions:
            connections_coords.add((cur_y, (int(cur_x) - 1)))
        if (cur_y, (int(cur_x) + 1)) in dots_positions:
            connections_coords.add((cur_y, (int(cur_x) + 1)))

    return connections_coords


rows = int(input())
board = [input() for _ in range(rows)]
dots_positions = find_dot_positions(board)
connections_made = find_connections(dots_positions)
max_length = len(connections_made)

print(max_length)
