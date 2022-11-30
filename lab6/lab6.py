def mul02(byte):
    byte_in_des = byte
    inpyt_byte_in_bin =  str(bin(byte_in_des))[2:]
    byte_shifted_in_des = byte_in_des << 1
    byte_shifted_in_bin = str(bin(byte_shifted_in_des))[2:]
    if len(byte_shifted_in_bin) > 8:
        byte_shifted_in_bin = byte_shifted_in_bin[len(byte_shifted_in_bin) - 8:]
        byte_shifted_in_des =  int(byte_shifted_in_bin, base=2)
    result = hex(byte_shifted_in_des)
    if len(inpyt_byte_in_bin) == 8 and inpyt_byte_in_bin[0] == '1':
        val_xor = '00011011'
        val_xor_in_dec = int(val_xor, base=2)
        result = hex(byte_shifted_in_des ^ val_xor_in_dec)
    result_str= str(result)[2:]
    if len(result_str) < 2:
        result_str = '0'+result_str
    return result_str

def mul03(byte):
    mul02_res = mul02(byte)
    mul02_res_in_des = int(mul02_res, base=16)
    byte_in_des = byte
    result = hex(mul02_res_in_des ^ byte_in_des)
    result_str = str(result)[2:]
    if len(result_str) < 2:
        result_str = '0' + result_str
    return result_str


byte1 = 0xd4
byte2 = 0xbf
print('Множення байту на елемент (байт) 02 та 03:')
print(f'mul02(d4): {mul02(byte1)}')
print(f'mul03(bf): {mul03(byte2)}')
