resources_dict = {"shards": 0, "fragments": 0, "motes": 0}
valuables = ["shards", "fragments", "motes"]
legendary_items = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
legendary_gotten = False

while not legendary_gotten:
    resources = input().split()

    for i in range(0, len(resources), 2):
        resource = resources[i + 1].lower()
        quant = int(resources[i])
        resources_dict[resource] = resources_dict.get(resource, 0) + quant

        if resources_dict[resource] >= 250 and resource in valuables:
            legendary_gotten = True
            legendary_item = legendary_items[resource]
            resources_dict[resource] -= 250
            print(f"{legendary_item} obtained!")
            break

for resource, quant in resources_dict.items():
        print(f"{resource}: {quant}")
