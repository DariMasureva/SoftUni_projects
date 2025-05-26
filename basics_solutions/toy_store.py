vacation_price = float(input())
puzzle_count = int(input())
talking_doll_count = int(input())
teddy_count = int(input())
minion_count = int(input())
truck_count = int(input())

puzzle_price = 2.60
talking_doll_price = 3
teddy_price = 4.10
minion_price = 8.20
truck_price = 2

discount = 0

price = puzzle_price * puzzle_count \
        + talking_doll_price * talking_doll_count\
        + teddy_price * teddy_count \
        + minion_price * minion_count \
        + truck_price * truck_count

total_count = puzzle_count + talking_doll_count + teddy_count + minion_count + truck_count

if total_count >= 50:
    discount = 0.25

profit = (price - price * discount) * 0.9

if profit >= vacation_price:
    leftover = profit - vacation_price
    print(f"Yes! {leftover:.2f} lv left.")
else:
    leftover = vacation_price - profit
    print(f"Not enough money! {leftover:.2f} lv needed")
