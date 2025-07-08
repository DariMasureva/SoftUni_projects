resources = {}

while True:
    command = input()
    if command == "stop":
        break

    resource = command
    quant = int(input())

    resources[resource] = resources.get(resource, 0) + quant

for resource, quant in resources.items():
    print(f"{resource} -> {quant}")
