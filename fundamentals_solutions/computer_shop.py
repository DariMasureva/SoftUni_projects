prices = []

while True:
    command = input()
    if command in "special regular":
        break

    price = float(command)
    if price < 0:
        print("Invalid price!")
        continue

    prices.append(price)

price_no_tax = sum(prices)
taxes = price_no_tax * 0.2
total = price_no_tax + taxes

if command == "special":
    total *= 0.9

if total == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {price_no_tax:.2f}$\n"
          f"Taxes: {taxes:.2f}$\n"
          "-----------\n"
          f"Total price: {total:.2f}$")
