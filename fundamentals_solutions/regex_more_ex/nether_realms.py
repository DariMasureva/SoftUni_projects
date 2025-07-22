import re

# the names are separated and stripped from unnecessary spaces, then sorted alphabetically
demon_names = list(sorted([name.strip() for name in input().split(",")]))
health_pattern = r"[^0-9\.\+\-\*\/]"
damage_pattern = r"[+|\-]?\d+\.?\d*"

for cur_demon in demon_names:
    # finding all valid symbols and the sum of their ascii codes
    cur_health = sum(ord(symbol) for symbol in re.findall(health_pattern, cur_demon))

    # mapping all numbers into ints and then finding their sum
    base_damage = sum(map(float, re.findall(damage_pattern, cur_demon)))

    for symbol in cur_demon:
        if symbol == "/":
            base_damage /= 2
        elif symbol == "*":
            base_damage *= 2

    print(f"{cur_demon} - {cur_health} health, {base_damage:.2f} damage")
