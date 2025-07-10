def sum_hat_color(cur_color_: str, all_hat_colors: list):
    cur_color_sum = sum([1 for color in all_hat_colors if color == cur_color_])
    return cur_color_sum


dwarves = []

while (new_dwarf_info := input()) != "Once upon a time":
    name, hat_color, physique = new_dwarf_info.split(" <:> ")
    physique = int(physique)
    dwarf_already_stored = False

    # iterating through the already existing dwarves to find matches
    for idx, cur_dwarf_info in enumerate(dwarves):
        cur_name = cur_dwarf_info["name"]
        cur_color = cur_dwarf_info["hat color"]
        cur_physique = cur_dwarf_info["physique"]

        # only case in which the new dwarf is stored in another way
        if cur_name == name and cur_color == hat_color:
            dwarves[idx]["physique"] = max(dwarves[idx]["physique"], physique)
            dwarf_already_stored = True
            break

    if not dwarf_already_stored:
        dwarves.append({"name": name, "hat color": hat_color, "physique": physique})

# extracting all hat colors to facilitate function further on
all_hat_colors_ = [dwarf["hat color"] for dwarf in dwarves]

# sorting
dwarves = list(
    sorted(dwarves, key=lambda dwarf: (dwarf["physique"], sum_hat_color(dwarf["hat color"], all_hat_colors_)),
           reverse=True))

# output
for dwarf in dwarves:
    print(f"({dwarf['hat color']}) {dwarf['name']} <-> {dwarf['physique']}")
