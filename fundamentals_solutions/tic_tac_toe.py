field = [input(),
         input(),
         input()]

for line in field:
    line = line.split(" ")
    one_equals = False
    two_equals = False
    one_diagonal = False
    two_diagonal = False

    if line[0] == line[1] == line[2] and line[1] != "0":
        if line[0] == "1":
            one_equals = True
        elif line[0] == "2":
            two_equals = True

    if one_equals or two_equals:
        break

if field[0][4] == field[1][2] == field[2][0] or field[0][0] == field[1][2] == field[2][4]:
    if field[1][2] == "1":
        one_diagonal = True
    elif field[1][2] == "2":
        two_diagonal = True

if one_diagonal or one_equals:
    print("First player won")
elif two_equals or two_diagonal:
    print("Second player won")
else:
    print("Draw!")
