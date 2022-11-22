from utils import *


range_end = 10000
p = generate_prime_value(range_end)
q = generate_prime_value(range_end)
while q == p:
    q = generate_prime_value(range_end)
n = p * q
pfi = (p - 1) * (q - 1) # phi(n)
is_valid= False
while is_valid != True:
    e = random.randint(1, pfi)
    if gcdex(e, pfi)[0] == 1:
        is_valid = True

d = inverse_element(e, pfi)
public_key = (n,e)
private_ker = (n,d)

m = input("Введіть число в межах від 1 до {}: ".format(n - 2))
try:
    m = int(m)
    if m < 1 or m > n - 2:
    	raise ValueError
    c = coding(m, public_key)
    print('Зашифроване число:',c)
    m = encoding(c, private_ker)
    print('Розшифроване число:', m)
except:
    print("Ви ввели не число або число у неправильному діапазоні!")
    print("Спробуйте ще раз!")
