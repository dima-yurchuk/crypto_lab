import random
from lab4.utils import *


def test_Miller_Rabin(n, a):
    if gcdex(n, a)[0] > 1:
        return False
    s = 0
    n_copy = n - 1
    while n_copy % 2 == 0:
        s += 1
        n_copy /= 2
    d = (n - 1) // 2 ** s
    x = pow(a, d, n)
    if x == 1 or x == -1:
        return True
    for i in range(1, s):
        if pow(x, 2 ** i, n) == 1:
            return False
        if pow(x, 2 ** i, n) == -1:
            return True
    return True

def is_prime(n):
    for i in range(0,100):
        a = random.randint(0,n)
        if not test_Miller_Rabin(n, a):
            return False
    return True

def generate_prime_value(range_end):
    is_prime_value = False
    while is_prime_value != True:
        value = random.randint(3, range_end)
        if is_prime(value):
            is_prime_value = True
    return value

def coding(m, public_key):
    n = public_key[0]
    e = public_key[1]
    c = pow(m, e, n)
    return c

def encoding(c, private_ker):
    n = private_ker[0]
    d = private_ker[1]
    m = pow(c, d, n)
    return m