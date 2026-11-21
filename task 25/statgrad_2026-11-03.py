'''Пусть M – сумма двух наибольших простых натуральных делителей целого числа, не считая самого числа.
Если таких делителей у числа нет, то значение М считается равным нулю.
Напишите программу, которая перебирает целые числа, бо́льшие 8 007 459 808, в порядке возрастания и
ищет среди них такие, у которых значение M больше 70 000, является простым числом и в своём
написании содержит последовательность цифр 23 (23 – идущие подряд друг за другом в указанном порядке цифры 2 и 3)
ровно один раз. В ответе запишите для первых 5 найденных чисел соответствующие им значения M.'''

def good(n):
    de = []
    for d in range(2, round(n ** 0.5) + 1):
        if n % d == 0:
            if isprime(d):
                de.append(d)
            if isprime(n // d) and n // d not in de:
                de.append(n // d)
    if len(de) >= 2:
        m = sum(sorted(de)[-2:])
        if m > 70_000 and isprime(m) and str(m).count('23') == 1:
            return m
    return 0

def isprime(n):
    for d in range(2, round(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True

from datetime import datetime

t1 = datetime.now()
k = 0
for x in range(8_007_459_809, 8_010_000_000):
    y = good(x)
    if y:
        print(y)
        k += 1
    if k == 5:
        break
t2 = datetime.now()
print(t2 - t1)

print(isprime(10000019 - 150))