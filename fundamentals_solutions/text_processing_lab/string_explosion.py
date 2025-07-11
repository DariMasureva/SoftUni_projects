initial_input = list(input())
last_expl_idx = 0

for idx, char in enumerate(initial_input):
    if char == ">":
        last_expl_idx = idx
        chars_exploded = int(initial_input[idx + 1])
        target = initial_input[idx+1:idx+1+chars_exploded]

        for _ in range(target.count(">")):
            last_expl_idx = target.index(">")
            chars_exploded += int(target[last_expl_idx + 1])