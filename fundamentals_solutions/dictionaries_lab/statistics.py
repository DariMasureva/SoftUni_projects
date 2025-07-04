products = {}

while True:
    command = input()
    if command == "statistics":
        print("Products in stock:")
        for (product, quantity) in products.items():
            print(f"- {product}: {quantity}")
        print(f"Total Products: {len(products.keys())}")
        print(f"Total Quantity: {sum(products.values())}")
        break

    command = command.split(": ")
    product = command[0]
    quantity = int(command[1])

    if product not in products:
        products[product] = 0

    products[product] += quantity
