from utils import *
from lab9.utils import *
import random


point = (0, 14)
a = 15
module = 43
point_order = find_order_point(point, module, a)

input_text = input("Введіть повідомлення для підпису:\n")
H = sha1(input_text)
h = pow(int(H, base=16), 1, point_order)
# print('Перевірка на тестовому прикладі з книжки:')
# print('-------------------------------------------')
# h = 4
r, s, Q = singing(point, a, module, point_order, h)

print(f'Підписане повідомлення: ("{input_text}", {r}, {s}, text)')
# print(f'Підписане повідомлення: (Хеш - {h}, {r}, {s}, text)')

print("Перевірка валідності підпису:",
      verify_signature(r, s, point_order, Q, point, module, a, h))