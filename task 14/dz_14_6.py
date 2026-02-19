'''
Значение арифметического выражения
5²⁰ + 5¹⁰ − 5¹³ − 5³
записали в системе счисления с основанием 5.

Определите сумму цифр в записи этого числа.
'''


def per(n, q):
    if n == 0:
        return '0'
    alf = '0123456789abcdefghijklmnopqrstuvwxyz'
    s = ''
    while n > 0:
        s = alf[n % q] + s
        n //= q
    return s

n = 5 ** 20 + 5 ** 10 - 5 ** 13 - 5 ** 3
xx = per(n, 5)
s = sum(int(x) for x in xx)
print(xx, s)