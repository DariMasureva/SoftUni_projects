import re

furniture_bought = []
total_cost = 0
pattern = r"^>>([a-zA-Z]+)<<(\d+\.?\d+)!(\d+)$"

while (product_info := input()) != "Purchase":
    cur_product = re.search(pattern, product_info)
    if cur_product:
        name, price, quantity = cur_product.groups()
        furniture_bought.append(name)
        total_cost += int(quantity) * float(price)

print("Bought furniture:")
for furniture in furniture_bought:
    print(furniture)
print(f"Total money spend: {total_cost:.2f}")
