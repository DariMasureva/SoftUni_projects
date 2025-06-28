def find_paths(board:list, position:tuple):
    paths_found = []
    x = position[0]
    y = position[1]
    next_x_valid = 0 <= x + 1 < len(board[y])
    next_y_valid = 0 <= y < len(board)
    prev_x_valid = 0 <= x - 1 < len(board[y])
    prev_y_valid = 0 <= y - 1 < len(board)

    if next_x_valid and board[y][x+1] == " ":
        paths_found.append([(x+1, y)])
    elif next_y_valid and board[y+1][x] == " ":
        paths_found.append([(x, y+1)])
    elif prev_y_valid and board[y-1][x] == " ":
        paths_found.append([(x, y-1)])
    elif prev_x_valid and board[x-1][y] == " ":
        paths_found.append([(x-1, y)])

    return paths_found

rows = int(input())
field = [input() for _ in range(rows)]

for idx, row in enumerate(field):
    if "k" in row:
        kates_position = (row.index("k"), idx)
        break

paths = find_paths(field, kates_position)
print(paths)
