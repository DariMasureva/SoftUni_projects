def format_attacks(initial_input):
    formatted = []
    separated_attacks = initial_input.split(" ")

    for attack in separated_attacks:
        attack = attack.split("-")
        formatted.append((int(attack[0]), int(attack[1])))

    return formatted


rows = int(input())
field = [list(map(int, input().split())) for _ in range(rows)]
attacks = format_attacks(input())
ships_destroyed = 0

for attack_ in attacks:
    row = attack_[0]
    column = attack_[1]
    ship_attacked = field[row][column]

    if ship_attacked > 0:
        ship_attacked -= 1
        del field[row][column]
        field[row].insert(column, ship_attacked)
    else:
        continue

    if ship_attacked <= 0:
        ships_destroyed += 1

print(ships_destroyed)
