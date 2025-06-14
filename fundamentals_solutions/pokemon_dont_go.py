pokemon_list = list(map(int, input().split()))
captured_pokemon = []

while pokemon_list:
    cur_idx = int(input())
    length = len(pokemon_list)

    if cur_idx < 0:
        cur_element = int(pokemon_list[0])
        pokemon_list[0] = pokemon_list[-1]
    elif cur_idx >= length:
        cur_element = int(pokemon_list[-1])
        pokemon_list[-1] = pokemon_list[0]
    else:
        cur_element = int(pokemon_list.pop(cur_idx))

    captured_pokemon.append(cur_element)
    pokemon_list = [value + cur_element if value <= cur_element else value - cur_element for value in pokemon_list]

print(sum(captured_pokemon))
