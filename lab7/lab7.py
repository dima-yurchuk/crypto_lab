from utils import *

input_matrix = [
    [0x32, 0x88, 0x31, 0xe0],
    [0x43, 0x5a, 0x31, 0x37],
    [0xf6, 0x30, 0x98, 0x07],
    [0xa8, 0x8d, 0xa2, 0x34]
]
key = [
    0x2b, 0x28, 0xab, 0x09,
    0x7e, 0xae, 0xf7, 0xcf,
    0x15, 0xd2, 0x15, 0x4f,
    0x16, 0xa6, 0x88, 0x3c
]

print('Матриця для шифрування:')
for i in range(len(input_matrix)):
    for j in range(len(input_matrix[i])):
        print(hex(input_matrix[i][j]), end=' ')
    print()
print('----------------------------------------')
encrypted_val = encrypt(input_matrix, key)
print('Зашифрована матриця:')
for i in range(len(encrypted_val)):
    for j in range(len(encrypted_val[i])):
        print(hex(encrypted_val[i][j]), end=' ')
    print()
print('----------------------------------------')
print('Розшифрована матриця:')
decrypted_val = decrypt(encrypted_val, key)

for i in range(len(decrypted_val)):
    for j in range(len(decrypted_val[i])):
        print(hex(decrypted_val[i][j]), end=' ')
    print()