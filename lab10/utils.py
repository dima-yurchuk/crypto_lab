from lab8.utils import *
from lab4.utils import *
import random


def generate_params():
    p = generate_prime_value(3000, 10000)
    g = get_g(p)
    x = random.randint(1, p-2)
    y = pow(g, x, p)
    return p, g, x, y


def singing(p, g, x, y, m):
    k = generate_prime_value(2, p - 2)
    r = pow(g, k, p)
    s = ((m - x*r) * inverse_element(k, p-1)) % (p - 1)
    return k, r, s


def verify_signature(r, p, s, m, y, g):
    if not (0 < r < p or 0 < s < p - 1):
        return False
    temp = (pow(y, r) * pow(r, s)) % p
    if pow(g, m, p) != temp:
        return False
    return  True


def get_H(m, p):
    H = 0
    for ch in m:
        H += ord(ch)
    if H > p - 1:
        H = H % p
    return H