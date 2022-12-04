import random
from utils import *

print('------------------------------------------------')
print('Обмін ключами по протоколу Діффі-Хелмана:')
p = generate_prime_value(3, 50)
g = get_g(p)
a = random.randint(1, 30)
b = random.randint(1, 30)


A = pow(g, a, p)
B = pow(g, b, p)
key2 = pow(A, b, p)
key1 = pow(B, a, p)

print('Отримане значення B (User1 від User2):', B)
print('Отримане значення A (User2 від User1):', A)
print('Секретний ключ:', key1)
print('------------------------------------------------')
print('Алгоритм Ель-Гамаля:')
p = generate_prime_value(30, 100)
g = get_g(p)
x = random.randint(1, p)
y = pow(g, x, p)
public_key = (p, g, y)
private_key = x

flag = False
try:
    while not flag:
        m = int(input(f'Введіть число для шифрування (не більше за {p-1}):'))
        if m < p and m >= 0:
            flag = True
    (a, b) = encrypt(m, p, g, y)
    print(f'Зашифроване число: ({a} {b})')
    value = decrypt(a, b, x, p)
    print(f'Розшифроване число: {value}')

except:
    print('Ви ввели не число!')
