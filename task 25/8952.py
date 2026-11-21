'''(№ 8952) Напишите программу, которая перебирает целые числа, большие 7 200 000, в порядке возрастания
и ищет среди них числа, представимые в виде произведения ровно трёх различных простых множителей, каждый
из которых содержит в своей записи одновременно цифры 3 и 7. В ответе запишите первые пять чисел в порядке
возрастания, справа от каждого числа запишите его наибольший простой делитель.'''

def isprime(n):
    for d in range(2, round(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True

def good_two(n):
    for d in prime37:
        if n % d == 0 and n // d in prime37:
            return (d, n // d)
    return ()

def good(x):
    de = set()
    for d in prime37:
        if x % d == 0:
            de.add(d)
            y = good_two(x // d)
            if y:
                de.add(y[0])
                de.add(y[1])
                if len(de) == 3:
                    return de
    return set()

from datetime import datetime

t1 = datetime.now()
prime37 = [x for x in range(37, 100_000, 2) if isprime(x) and '3' in str(x) and '7' in str(x)]
print(len(prime37))
k = 0
for x in range(7_200_001, 7_500_000):
    y = good(x)
    if y:
        print(x, max(y))
        k += 1
    if k == 5:
        break
t2 = datetime.now()
print(t2 - t1)