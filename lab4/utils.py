# extended Euclid algorithm
def gcdex(a,b):  # extended Euclid algorithm
    (a0, a1) = a, b
    (x0, x1) = 1, 0
    (y0, y1) = 0, 1
    while a1 != 0:
        q = a0 // a1
        (a0, a1) = (a1, a0-a1*q)
        (x0, x1) = (x1, x0 - x1 * q)
        (y0, y1) = (y1, y0 - y1 * q)
    return (a0, x0, y0)


# finding the multiplicative inverse element a^(-1) by modulo n
def inverse_element(a,n):
    d, x, y = gcdex(a, n)
    if d == 1:
        return x % n
    else:
        return f'Числа {a} і {n} не взаємно прості!'


# value of the Euler function
def phi(m):
    m_input = m
    output = {}
    i = 2
    k = 0
    while m % i == 0:
        m = m // i
        k += 1
    if k > 0:
        output[i] = k
    i = 3
    break_flag = False
    while i * i <= m:
        k = 0
        for elem in output:
            if i * i > m:
                break_flag = True
                break
            if i % elem == 0:
                i += 2
        if break_flag:
            break
        while m%i == 0:
            m = m // i
            k += 1
        if k > 0:
            output[i] = k
        i += 2
    res = m_input
    if m != 1:
        output[m] = 1
    for elem in output:
        res *= (1 - (1/elem))
    return int(res)


# finding the multiplicative inverse element a^(-1) by modulo n
def inverse_element_2(a,n):
    pfi_n = phi(n)
    return (a ** (pfi_n - 1)) % n