def average_type_stats(type_info):
    damage_avrg = sum([cur_stats["damage"] for cur_stats in type_info.values()]) / len(type_info)
    health_avrg = sum([cur_stats["health"] for cur_stats in type_info.values()]) / len(type_info)
    armor_avrg = sum([cur_stats["armor"] for cur_stats in type_info.values()]) / len(type_info)

    return damage_avrg, health_avrg, armor_avrg

dragons = {}
dragons_count = int(input())
defaults = {"damage": 45, "health": 250, "armor": 10}

for _ in range(dragons_count):
    # extracting info
    type_, name, damage, health, armor = input().split()
    # formatting to update main dict and set defaults more easily
    stats = {"damage": damage, "health": health, "armor": armor}
    # replacing nulls with default values from the defaults dict
    stats = {stat_name:(int(value) if value != "null" else defaults[stat_name]) for stat_name, value in stats.items()}
    if type_ not in dragons:
        dragons[type_] = {}

    dragons[type_][name] = stats

for type_, type_stats in dragons.items():
    # sorting alphabetically by name
    type_stats = dict(sorted(type_stats.items(), key=lambda item: item[0]))
    # getting average stats
    average_damage, average_health, average_armor = average_type_stats(type_stats)

    print(f"{type_}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})")

    for name, dragon_stats in type_stats.items():
        print(f"-{name} -> damage: {dragon_stats['damage']}, health: {dragon_stats['health']}, armor: {dragon_stats['armor']}")
