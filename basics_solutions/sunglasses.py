n = int(input())
rows = n
columns = 5 * n

if n % 2 == 0:
    center_row = n / 2 - 1
else:
    center_row = n // 2

for row in range(n):

    if row == 0 or row == n - 1:

        for _ in range(n * 2):
            print("*", end="")
        for _ in range(n):
            print(" ", end="")
        for _ in range(n * 2):
            print("*", end="")

        print("", end="\n")

    elif row == center_row:
        for column in range(columns):

            if column == 0 or (column == 2 * n - 1) or (column == 3 * n) or (column == columns - 1):
                print("*", end="")

            elif 0 < column < (n * 2 - 1) or (3 * n) < column < (5 * n - 1):
                print("/", end="")
            else:
                print("|", end="")

        print()

    else:
        for column in range(columns):

            if column == 0 or (column == 2 * n - 1) or (column == 3 * n) or (column == columns - 1):
                print("*", end="")

            elif 0 < column < (n * 2 - 1) or (3 * n) < column < (5 * n - 1):
                print("/", end="")
            else:
                print(" ", end="")

        print()
