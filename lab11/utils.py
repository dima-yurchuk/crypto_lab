from lab4.utils import *
import random

def get_all_poins_elliptic_curve(count):
    arr = []
    for x in range(count):
        for y in range(count):
            # if (pow(y, 2) - (pow(x, 3) + 15 * x + 24)) % count == 0:
            if (pow(y, 2) - (pow(x, 3) + x + 1)) % count == 0:
                arr.append((x, y))
    return arr


def add_point(first_point, second_point, count, a):
    if first_point != second_point:
        numerator = second_point[1] - first_point[1]
        denominator = second_point[0] - first_point[0]
        temp = pow(inverse_element(denominator, count), 1, count) * numerator
        s = pow(temp, 1, count)
        x = pow(pow(s, 2) - (second_point[0] + first_point[0]), 1, count)
        y = pow(s * (second_point[0] - x) - second_point [1], 1, count)
    else:
        numerator = 3 * pow(first_point[0], 2) + a
        denominator = 2 * first_point[1]
        temp = pow(inverse_element(denominator, count), 1, count) * numerator
        s = pow(temp, 1, count)
        x = pow(pow(s, 2) - 2 * first_point[0], 1, count)
        y = pow(s * (first_point[0] - x) - first_point[1], 1, count)
    return (x, y)


def find_order_point(first_point, count, a):
    second_point = add_point(first_point, first_point, count, a)
    d = 2
    while first_point[0] != second_point[0]:
        d += 1
        second_point = add_point(first_point, second_point, count, a)
    d += 1
    return d


def singing(point, a, module, point_order, h):
    Q = point
    d = random.randint(2, point_order - 2)
    # d = 5
    for i in range(d-1):
        Q = add_point(Q, point, module, a)
    k = random.randint(2, point_order - 2)
    # k = 2

    C = point
    for i in range(0, k - 1):
        C = add_point(C, point, module, a)
    r = pow(C[0], 1, point_order)

    temp = inverse_element(k, point_order)
    s = pow((h + d * r) * temp, 1, point_order)
    return r, s, Q


def verify_signature(r, s, point_order, Q, point, module, a, h):
    u = pow(h * inverse_element(s, point_order), 1, point_order)
    v = pow(r * inverse_element(s, point_order), 1, point_order)
    point_first = point
    point_second = Q
    for i in range(u - 1):
        point_first = add_point(point_first, point, module, a)
    for i in range(v - 1):
        point_second = add_point(point_second, Q, module, a)
    final_point = add_point(point_first, point_second, module, a)
    r_h = pow(final_point[0], 1, point_order)
    return r == r_h
