products = {}

while True:
    product_info = input().split()
    if product_info[0] == "buy":
        break

    name, price, quantity = product_info
    price = float(price)
    quantity = int(quantity)

    if products.get(name):
        quantity = products[name][1] + quantity

    products[name] = [price, quantity]

for cur_product, cur_info in products.items():
    cur_total = cur_info[0] * cur_info[1]
    print(f"{cur_product} -> {cur_total:.2f}")
