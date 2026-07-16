'''Пусть M – сумма наименьшего и наибольшего простых делителей числа.
Напишите программу, которая перебирает целые числа, превышающие 8 007 000 000, такие
что для них число M простое, больше 80000 и содержит ровно один раз в своей записи
последовательность цифр «567».
В ответе запишите первые пять найденных чисел в порядке возрастания'''

from datetime import datetime

def isprime(x):
    for d in range(2, round(x ** 0.5) + 1):
        if x % d == 0:
            return False
    return True

def good(x):
    de = []
    for d in range(2, round(x ** 0.5) + 1):
        if x % d == 0:
            if isprime(d):
                de.append(d)
            if isprime(x // d):
                de.append(x // d)
    if de:
        m = max(de) + min(de)
        if isprime(m) and m > 80000 and str(m).count('567') == 1:
            return m
    return 0

t1 = datetime.now()
x = 8_007_000_001
k = 0
while k < 5:
    y = good(x)
    if y:
        print(x, y)
        k += 1
    x += 1
t2 = datetime.now()
print(t2 - t1)