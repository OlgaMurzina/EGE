'''
Напишите программу, которая перебирает целые числа, большие 5_000_000, в порядке возрастания
и ищет среди них числа, представимые в виде произведения ровно трех простых множителей, необязательно
различных, каждый из которых содержит в своей записи хотя бы одну цифру 2 или 3.
В ответе запишите первые пять чисел в порядке возрастания.
'''
def isprime(x):
    for d in range(2, round(x ** 0.5) + 1):
        if x % d == 0:
            return False
    return True

def two_primes(x):
    de = []
    for d in range(2, round(x**0.5)+ 1):
        if x%d== 0:
            if isprime(d) and isprime(x // d):
                if ('2' in str(d) or '3' in str(d)) and ('2' in str(x // d) or '3' in str(x // d)):
                    de.append(d)
                    de.append(x // d)
    return de


def good(x):
    de = []
    for d in range(2, round(x**0.5)+ 1):
        if x%d== 0:
            if isprime(d):
                if ('2' in str(d) or '3' in str(d)):
                    y = two_primes(x // d)
                    if y:
                        de.append(d)
                        de.extend(y)
    return de


k = 0
x = 5_000_001
while k < 5:
    y = good(x)
    if y:
        k += 1
        print(x, y)
    x += 1