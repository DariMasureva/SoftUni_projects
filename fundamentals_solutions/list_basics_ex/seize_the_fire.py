fires = input().split("#")
water = int(input())
cell_values = []
effort = 0

for fire in fires:
    fire_split = fire.split("=")
    cell_value = int(fire_split[1])

    if ("High" in fire and 81 <= cell_value <= 125) or\
       ("Medium" in fire and 51 <= cell_value <= 80) or\
       ("Low" in fire and 1 <= cell_value <= 50):

        if water >= cell_value:
            water -= cell_value
            cell_values.append(cell_value)
            effort += cell_value * 0.25

print("Cells:")

for cell_value in cell_values:
    print(f" - {cell_value}")

print(f"Effort: {effort:.2f}\n"
      f"Total Fire: {sum(cell_values)}")
