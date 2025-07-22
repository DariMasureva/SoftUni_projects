import re

valid_order_pattern = r"^%([A-Z][a-z]+)%[^\.$%|]*<([\w]+)>[^\.$%|]*\|(\d+)\|[^\.$%|\d]*(\d+\.?\d+)\$$"
total_income = 0

while (order := input()) != "end of shift":
    check = re.search(valid_order_pattern, order)

    if check:
        customer, product, count, price = check.groups()
        total_price = float(price) * int(count)
        total_income += total_price
        print(f"{customer}: {product} - {total_price:.2f}")

print(f"Total income: {total_income:.2f}")