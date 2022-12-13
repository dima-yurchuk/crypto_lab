from utils import *

arr = get_all_poins_elliptic_curve(23)
print("Всі точки еліптичної кривої:")
for idx, elem in enumerate(arr):
    print(elem, end=', ')
    if (idx+1) % 7 == 0:
        print()
print(f'\nКількість точок: {len(arr)}')


print("------------------------------------------------------------------")
point = (17, 20)
print(f'Порядок точки G = {point} на еліптичній кривій: '
      f'{find_order_point(point, 23)}')