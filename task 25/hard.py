'''Напишите программу, которая перебирает целые числа, большие 1_103_285_717,
в порядке возрастания и ищет среди них числа, представленные в виде произведения
ровно двух простых множителей, не обязательно различных, каждый из которых содержит
ровно один раз в своей записи последовательность цифр «16».
В ответе запишите в первом столбце таблице первые пять найденных чисел в порядке возрастания,
во втором столбце – для каждого из них наименьший найденный множитель для каждого из них.'''

def is_prime(x):
    for d in range(2, round(x ** 0.5) + 1):
        if x % d == 0:
            return False
    return True

def good(n):
    de = []
    for d in range(2, round(n ** 0.5) + 1):
        if n % d == 0:
            if is_prime(d) and is_prime(n // d) and str(d).count('16') == 1 and str(n // d).count('16') == 1:
                de.append(d)
                de.append(n // d)
                break
    if len(de) == 2:
        return min(de)
    return 0

from datetime import datetime
t1 = datetime.now()
k = 0
for x in range(1_103_285_717 + 1, 1_105_285_717):
    y = good(x)
    if y:
       print(x, y)
       k += 1
    if k == 5:
       break
t2 = datetime.now()
print(t2 - t1)
print()

from datetime import datetime
t1 = datetime.now()
prime_16 = [x for x in range(2, 100_000) if is_prime(x) and str(x).count('16') == 1]
print(prime_16[:5])
k = 0
for x in range(1_103_285_717 + 1, 1_105_285_717):
    for d in prime_16:
        if x % d == 0 and is_prime(x // d) and str(x // d).count('16') == 1:
            print(x, min(d, x// d))
            k += 1
            break
    if k == 5:
        break
t2 = datetime.now()
print(t2 - t1)