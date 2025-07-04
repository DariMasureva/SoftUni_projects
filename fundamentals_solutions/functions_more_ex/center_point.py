from math import floor


def closest_point(x1, y1, x2, y2):

    dist_1 = (x1 ** 2 + y1 ** 2)
    dist_2 = (x2 ** 2 + y2 ** 2)

    if dist_1 <= dist_2:
        return x1, y1
    else:
        return x2, y2


x1_ = float(input())
y1_ = float(input())
x2_ = float(input())
y2_ = float(input())

closest_x, closest_y = closest_point(x1_, y1_, x2_, y2_)

print(f"({floor(closest_x)}, {floor(closest_y)})")
