events = input().split("|")
energy = 100
coins = 100

for event in events:
    event_split = event.split("-")
    task = event_split[0]
    value = int(event_split[1])

    if task == "rest":
        if energy + value >= 100:
            value = 100 - energy
            energy = 100
        else:
            energy += value

        print(f"You gained {value} energy.")
        print(f"Current energy: {energy}.")

    elif task == "order":
        if energy >= value:
            coins += value
            energy -= 30
            print(f"You earned {value} coins.")
        else:
            if energy + 50 >= 100:
                energy = 100
            else:
                energy += 50
            print("You had to rest!")

    else:
        if value <= coins:
            coins -= value
            print(f"You bought {task}.")
        else:
            print(f"Closed! Cannot afford {task}.")
            break

else:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")
