plant_count = int(input())
plants = {}

for _ in range(plant_count):
    plant_name, rarity = input().split("<->")
    if plant_name in plants.keys():
        plants[plant_name]["Rarity"] = int(rarity)
    else:
        plants[plant_name] = {"Rarity": int(rarity), "Rating": []}

while (command := input()) != "Exhibition":
    action_name, action_specifications = command.split(": ")
    error_found = False

    match action_name:
        case "Rate":
            cur_plant, rating = action_specifications.split(" - ")
            if cur_plant not in plants:
                error_found = True
            else:
                plants[cur_plant]["Rating"].append(int(rating))
        case "Update":
            cur_plant, new_rarity = action_specifications.split(" - ")
            if cur_plant not in plants:
                error_found = True
            else:
                plants[cur_plant]["Rarity"] = int(new_rarity)
        case "Reset":
            cur_plant = action_specifications
            if cur_plant not in plants:
                error_found = True
            else:
                plants[cur_plant]["Rating"].clear()

    if error_found:
        print("error")

print("Plants for the exhibition:")
for plant_name, cur_stats in plants.items():
    rarity, ratings = cur_stats.values()
    if len(ratings) > 0:
        avrg_rating = sum(ratings) / len(ratings)
    else:
        avrg_rating = 0

    print(f"- {plant_name}; Rarity: {rarity}; Rating: {avrg_rating:.2f}")
