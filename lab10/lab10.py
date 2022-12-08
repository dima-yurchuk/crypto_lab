from utils import *


p, g, x, y = generate_params()
m = input('Введіть повідомлення для підпису:\n')
H = get_H(m, p)
k, r, s = singing(p, g, x, y, H)
print(f'Підписане повідомлення: ("{m}", {r}, {s})')
print("Перевірка валідності підпису:", verify_signature(r, p, s, H, y, g))