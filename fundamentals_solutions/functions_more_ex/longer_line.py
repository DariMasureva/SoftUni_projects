from math import floor


def closest_point(x1, y1, x2, y2):

    dist_1 = (x1 ** 2 + y1 ** 2)
    dist_2 = (x2 ** 2 + y2 ** 2)

    if dist_1 <= dist_2:
        return x1, y1, x2, y2
    else:
        return x2, y2, x1, y1


def longest_line(x1, y1, x2, y2, x3, y3, x4, y4):

    if x1 == x2:
        line_1_len = abs(y1 - y2)
    elif y1 == y2:
        line_1_len = abs(x1 - x2)
    else:
        line_1_len = (abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) ** 0.5

    if x3 == x4:
        line_2_len = abs(y3 - y4)
    elif y3 == y4:
        line_2_len = abs(x3 - x4)
    else:
        line_2_len = (abs(x3 - x4) ** 2 + abs(y3 - y4) ** 2) ** 0.5

    if line_1_len >= line_2_len:
        ordered_coords = closest_point(x1, y1, x2, y2)
    else:
        ordered_coords = closest_point(x3, y3, x4, y4)

    return ordered_coords


x1_ = float(input())
y1_ = float(input())
x2_ = float(input())
y2_ = float(input())
x3_ = float(input())
y3_ = float(input())
x4_ = float(input())
y4_ = float(input())

closest_x, closest_y, farthest_x, farthest_y = longest_line(x1_, y1_, x2_, y2_, x3_, y3_, x4_, y4_)
print(f"({floor(closest_x)}, {floor(closest_y)})({floor(farthest_x)}, {floor(farthest_y)})")
