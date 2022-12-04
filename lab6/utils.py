def mul02(byte):
    byte_in_des = byte
    inpyt_byte_in_bin =  str(bin(byte_in_des))[2:]
    byte_shifted_in_des = byte_in_des << 1
    byte_shifted_in_bin = str(bin(byte_shifted_in_des))[2:]
    if len(byte_shifted_in_bin) > 8:
        byte_shifted_in_bin = byte_shifted_in_bin[len(byte_shifted_in_bin) - 8:]
        byte_shifted_in_des =  int(byte_shifted_in_bin, base=2)
    result = byte_shifted_in_des
    if len(inpyt_byte_in_bin) == 8 and inpyt_byte_in_bin[0] == '1':
        val_xor = '00011011'
        val_xor_in_dec = int(val_xor, base=2)
        result = byte_shifted_in_des ^ val_xor_in_dec
    return result


def mul03(byte):
    mul02_res = mul02(byte)
    mul02_res_in_des = mul02_res
    byte_in_des = byte
    result = mul02_res_in_des ^ byte_in_des
    return result