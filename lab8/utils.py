from lab5.utils import is_prime
import random

def generate_prime_value(range_start, range_end):
    is_prime_value = False
    while is_prime_value != True:
        value = random.randint(range_start, range_end)
        if is_prime(value):
            is_prime_value = True
    return value

def test_g(g, p):
    g = [pow(g, i, p) for i in range(1, p-1)]
    return len(set(g)) == p - 2

def get_g(p):
    while True:
        g = random.randint(2, p)
        if test_g(g, p):
            return g

def encrypt(value, p, g, y):
    k = random.randint(1, p - 1)
    a = pow(g, k, p)
    b = ((y ** k) * value) % p
    return (a, b)

def decrypt(a, b, x, p):
    value = (b * (a ** (p - 1 - x))) % p
    return value