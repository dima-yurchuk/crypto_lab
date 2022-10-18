import numpy as np
from utils import encode_decode

key_hor = "qwertyuiopa"
key_ver = "sdfghjklx"

text = input("Ведіть текст для шифрування (максимум 99 символів):\n")[:99]
arr = np.array(list(text))
arr_empty = np.empty(99-len(text), np.str)
arr = np.concatenate((arr, arr_empty), axis=0).reshape((9,11))


arr = np.insert(arr, 0, list(key_hor), axis=0)
arr = np.insert(arr, 0, list(' '+key_ver), axis=1)

print('--------------------------------------------------------')
print('Шифрування...')
arr_encrypt, text_encrypted = encode_decode(arr, key_hor, key_ver, True)
print('Матриця (зашифрована):\n', arr_encrypt)
print('Зашифрований текст:', text_encrypted)


print('--------------------------------------------------------')
print('Розшифрування...')
arr_decrypt, text = encode_decode(arr, key_hor, key_ver, False)
print('Матриця (розшифрована):\n', arr_decrypt)
print('Розшифрований текст:', text)
