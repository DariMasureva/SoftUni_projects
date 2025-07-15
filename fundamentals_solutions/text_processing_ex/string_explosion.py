initial_input = list(input())

explosions = [(idx, int(initial_input[idx+1])) for idx, char in enumerate(initial_input) if char == ">"]
explosions.append((0,0))
cluster_start = explosions[0][0]
cluster_len = explosions[0][1]

for idx, (bomb_idx, expl_magnitude) in enumerate(explosions[1:], start=1):
    last_bomb_idx, last_expl_magnitude  = explosions[idx-1]

    if last_bomb_idx + last_expl_magnitude >= bomb_idx:
        cluster_len += expl_magnitude

    if last_bomb_idx + last_expl_magnitude < bomb_idx or idx == len(explosions) - 1:
        cluster_end = cluster_start + cluster_len
        bomb_count = initial_input[cluster_start:cluster_end].count(">")
        cluster_end += bomb_count
        for del_idx, symbol in enumerate(initial_input[cluster_start:cluster_end], start=cluster_start):
            if symbol != ">":
                initial_input[del_idx] = "*"

        cluster_start = bomb_idx
        cluster_len = expl_magnitude

result = [symbol for symbol in initial_input if symbol != "*"]
print("".join(result))
