import math

racket_price = float(input())
racket_no = int(input())
sneakers_no = int(input())

sneakers_price = racket_price * 1 / 6
subtotal = racket_no * racket_price + sneakers_no * sneakers_price
equipment = subtotal * 0.2
total = subtotal + equipment
djok_total = math.floor(1/8 * total)
sponsor_total = math.ceil(7/8 * total)
print(f"Price to be paid by Djokovic {djok_total}")
print(f"Price to be paid by sponsors {sponsor_total}")