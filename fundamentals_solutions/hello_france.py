items = input().split("|")
items_bought = []
items_new_prices = []
budget = int(input())
profit = 0

for item in items:
    item_split = item.split("->")
    price = float(item_split[1])

    if not 0 <= price <= 1000:
        continue

    if (item_split[0] == "Clothes" and price <= 50) or\
       (item_split[0] == "Shoes" and price <= 35) or \
       (item_split[0] == "Accessories" and price <= 20.50):

        if price < budget:
            budget -= price
            items_bought.append(price)

for price in items_bought:
    price *= 1.4
    price = round(price, 2)
    items_new_prices.append(price)

profit = sum(items_bought) * 0.4
total = sum(items_new_prices) + budget

for item in items_new_prices:
    print(item, end=" ")
print()
print(f"Profit: {profit:.2f}")

if total >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")