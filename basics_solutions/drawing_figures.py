from math import ceil

n = int(input())

if n % 2 == 0:
    stars_count = 2
    rows_count = n - 1
    n_even = True
else:
    stars_count = 1
    rows_count = n
    n_even = False

first_section_rows = ceil(n / 2)
middle_dashes_count = 0
side_dash_half = int((n - stars_count - middle_dashes_count) / 2)

for row in range(rows_count):

    if row == 1 and not n_even:
        middle_dashes_count = 1
    elif row == 1 and n_even:
        middle_dashes_count = 2

    for _ in range(side_dash_half):
        print("-", end="")

    print("*", end="")

    for _ in range(middle_dashes_count):
        print("-", end="")

    if stars_count == 2:
        print("*", end="")

    for _ in range(side_dash_half):
        print("-", end="")

    if row < first_section_rows - 1:
        middle_dashes_count += 2
        side_dash_half -= 1
    else:
        middle_dashes_count -= 2
        side_dash_half += 1

    if middle_dashes_count < 0:
        middle_dashes_count = 0

    if row == rows_count - 2 and not n_even:
        stars_count = 1
    elif row == rows_count - 2:
        stars_count = 2
    elif not n_even:
        stars_count = 2

    if row != rows_count - 1:
        print()
