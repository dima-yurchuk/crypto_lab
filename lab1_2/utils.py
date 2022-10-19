import numpy as np
import random
import copy
import re

def encode_decode(arr, key_hor, key_ver, encode):
    list_hor = list(key_hor)
    list_ver = list(key_ver)
    if encode:
        random.shuffle(list_hor)
        random.shuffle(list_ver)
    arr_local = np.transpose(copy.deepcopy(arr))
    temp = copy.deepcopy(arr_local)
    for i in range(0, len(list_hor)):
        arr_local[i+1] = temp[np.where(arr[0]==list_hor[i])[0]][0]
    array_copy = copy.deepcopy(arr_local)
    arr_local = np.transpose(arr_local)
    temp = copy.deepcopy(arr_local)
    for i in range(0, len(list_ver)):
        arr_local[i+1] = temp[np.where(array_copy[0]==list_ver[i])[0]][0]
    arr_local_for_return = copy.deepcopy(arr_local)
    if encode:
        arr_local = np.transpose(arr_local)
    arr_local = np.delete(arr_local, 0,0)
    arr_local = np.delete(arr_local, 0,1)
    text_crypto = ''
    for row in arr_local:
        text_row = ''.join(row)
        if text_row != ' ':
            text_crypto = text_crypto + text_row
    text_encrypted = text_crypto.strip()
    return arr_local_for_return, text_encrypted

def encrypt_polybius_square(text, dict_alphabets):
    hor_coordinates = ''
    ver_coordinates = ''
    for char in text:
        hor_coordinates += dict_alphabets[char][0]
        ver_coordinates += dict_alphabets[char][1]
    list_encrypted_text = re.findall('..', hor_coordinates+ver_coordinates)
    return ' '.join(list_encrypted_text)

def decrypt_polybius_square(encrypted_text, dict_alphabets):
    hor_coordinates = encrypted_text[:len(encrypted_text)//2].replace(' ', '')
    ver_coordinates = encrypted_text[len(encrypted_text)//2:].replace(' ', '')
    dict_swap = {value: key for key, value in dict_alphabets.items()}
    text = ''
    for i in range(0, len(hor_coordinates)):
        text += dict_swap[hor_coordinates[i]+ver_coordinates[i]]
    return text