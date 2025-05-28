number = int(input())
current_year = number + 1

while True:
    current_year_set = set(str(current_year))

    if len(current_year_set) == len(str(current_year)):
        print(current_year)
        break

    current_year += 1
