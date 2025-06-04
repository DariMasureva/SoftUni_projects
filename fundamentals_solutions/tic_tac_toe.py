field = [input(),
         input(),
         input()]

one_vertical = False
two_vertical = False
one_diagonal = False
two_diagonal = False

for line in field:
    line = line.split(" ")
    one_horizontal = False
    two_horizontal = False

    if line[0] == line[1] == line[2] and line[1] != "0":
        if line[0] == "1":
            one_horizontal = True
        elif line[0] == "2":
            two_horizontal = True

    if one_horizontal or two_horizontal:
        break

if field[0][4] == field[1][2] == field[2][0] or\
        field[0][0] == field[1][2] == field[2][4]:

    if field[1][2] == "1":
        one_diagonal = True
    elif field[1][2] == "2":
        two_diagonal = True

if field[0][0] == field[1][0] == field[2][0]:
    if field[0][0] == "1":
        one_horizontal = True
    elif field[0][0] == "2":
        two_horizontal = True

elif field[0][2] == field[1][2] == field[2][2]:
    if field[0][2] == "1":
        one_horizontal = True
    elif field[0][2] == "2":
        two_horizontal = True

elif field[0][4] == field[1][4] == field[2][4]:
    if field[0][4] == "1":
        one_horizontal = True
    elif field[0][4] == "2":
        two_horizontal = True


if one_diagonal or one_horizontal or one_vertical:
    print("First player won")
elif two_horizontal or two_diagonal or two_vertical:
    print("Second player won")
else:
    print("Draw!")
