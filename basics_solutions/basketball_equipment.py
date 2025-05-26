annual_fee = int(input())

sneakers = 0.6 * annual_fee
outfit = 0.8 * sneakers
basketball = 0.25 * outfit
accessories = 0.2 * basketball

total = "{:.2f}".format(annual_fee + sneakers + outfit + basketball + accessories)

print(total)
