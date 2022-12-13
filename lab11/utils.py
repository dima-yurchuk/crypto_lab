from lab4.utils import *


def get_all_poins_elliptic_curve(count):
    arr = []
    for x in range(count):
        for y in range(count):
            if (pow(y, 2) - (pow(x, 3) + x + 1)) % count == 0:
                arr.append((x, y))
    return arr


def add_point(a, b, count):
    if a != b:
        numerator = b[1] - a[1]
        denominator = b[0] - a[0]
        temp = pow(inverse_element(denominator, count), 1, count) * numerator
        s = pow(temp, 1, 23)
        x = pow(pow(s, 2) - (b[0] + a[0]), 1, count)
        y = pow(s * (b[0] - x) - b [1] , 1, count)
    else:
        numerator = 3 * pow(a[0], 2) + 1
        denominator = 2 * a[1]
        temp = pow(inverse_element(denominator, count), 1, count) * numerator
        s = pow(temp, 1, 23)
        x = pow(pow(s, 2) - 2 * a[0], 1, count)
        y = pow(s * (a[0] - x) - a[1], 1, 23)
    return (x, y)


def find_order_point(point_first, count):
    point_second = add_point(point_first, point_first, count)
    d = 2
    while point_first[0] != point_second[0]:
        d += 1
        point_second = add_point(point_first, point_second, count)
    d += 1
    return d