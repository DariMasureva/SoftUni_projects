items = input().split("|")
items_bought = []
items_new_prices = []
budget = int(input())
profit = 0

for item in items:
    item = item.split("->")
    price = float(item[1])
    item_type = item[0]

    if not 0 <= price <= 1000:
        continue

    if (item_type == "Clothes" and price <= 50) or\
       (item_type == "Shoes" and price <= 35) or \
       (item_type == "Accessories" and price <= 20.50):

        if price <= budget:
            budget -= price
            items_bought.append(price)
            price *= 1.4
            items_new_prices.append(f"{price:.2f}")

profit = sum(items_bought) * 0.4
total = sum(items_bought) * 1.4 + budget

print(" ".join(items_new_prices))
print(f"Profit: {profit:.2f}")

if total >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
