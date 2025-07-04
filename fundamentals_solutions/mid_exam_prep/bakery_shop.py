food_available = []
total_sales = 0

while True:
    command = input().split()
    action = command[0]

    if action == "Complete":
        break

    quantity = int(command[1])
    food = command[2]

    if action == "Receive":
        if quantity <= 0:
            continue

        if food not in food_available:
            food_available.append(food)
            food_available.append(quantity)

        else:
            food_idx = food_available.index(food)
            food_available[food_idx + 1] += quantity

    elif action == "Sell":
        if food not in food_available:
            print(f"You do not have any {food}.")
            continue

        else:
            food_idx = food_available.index(food)

            if quantity > food_available[food_idx + 1]:
                quantity = food_available[food_idx + 1]
                food_available[food_idx + 1] = 0
                print(f"There aren't enough {food}. You sold the last {quantity} of them.")

            else:
                food_available[food_idx + 1] -= quantity
                print(f"You sold {quantity} {food}.")

            total_sales += quantity

            if food_available[food_idx + 1] == 0:
                food_available.pop(food_idx)
                food_available.pop(food_idx)


foods = food_available[::2]
quantities = [quant for quant in food_available if quant not in foods]

for food, quant in zip(foods, quantities):
    print(f"{food}: {quant}")
print(f"All sold: {total_sales} goods")
