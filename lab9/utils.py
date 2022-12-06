def split_bits(bits, length):
    return [bits[i:i + length] for i in range(0, len(bits), length)]


def cycle_shift(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xffffffff

def sha1(data):
    bits = ""
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    # convert char to bit
    for n in range(len(data)):
        bits+='{0:08b}'.format(ord(data[n]))

    bits = bits+"1"
    bit_length = len(bits)

    # add 0 bit until length equals 448 mod 512
    while len(bits)%512 != 448:
        bits+="0"
    # append the original length in bits
    bits+='{0:064b}'.format(bit_length-1)
    for c in split_bits(bits, 512):
        split_bits_32_len = split_bits(c, 32)
        w = [None for x in range(80)]
        for i in range(0, 16):
            w[i] = int(split_bits_32_len[i], 2)
        for i in range(16, 80):
            w[i] = cycle_shift((w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16]), 1)
        a = h0
        b = h1
        c = h2
        d = h3
        e = h4

        for i in range(0, 80):
            if 0 <= i <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= i <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= i <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            elif 60 <= i <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = cycle_shift(a, 5) + f + e + k + w[i] & 0xffffffff
            e = d
            d = c
            c = cycle_shift(b, 30)
            b = a
            a = temp

        h0 = h0 + a & 0xffffffff
        h1 = h1 + b & 0xffffffff
        h2 = h2 + c & 0xffffffff
        h3 = h3 + d & 0xffffffff
        h4 = h4 + e & 0xffffffff

    return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)