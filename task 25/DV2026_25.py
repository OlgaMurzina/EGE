'''Напишите программу, которая перебирает целые числа, большие 1 103 285 717, в порядке
возрастания и ищет среди них числа, представленные в виде произведения ровно двух про-
стых множителей, не обязательно различных, каждый из которых содержит ровно один раз в
своей записи последовательность цифр «16». В ответе запишите в первом столбце таблице
первые пять найденных чисел в порядке возрастания, во втором столбце – для каждого из
них наименьший найденный множитель для каждого из них.'''

from datetime import datetime

def isprime(x):
    for d in range(2, round(x ** 0.5) + 1):
        if x % d == 0:
            return False
    return True

def good(x):
    de = ()
    for d in range(2, round(x ** 0.5) + 1):
        if x % d == 0:
            if isprime(d) and isprime(x // d):
                if str(d).count('16') == 1 and str(x // d).count('16') == 1:
                    de = (d, x // d)
                    break
    return de

t1 = datetime.now()
x = 1_103_285_718
k = 0
while k < 5:
    y = good(x)
    if y:
        print(x, min(y))
        k += 1
    x += 1
t2 = datetime.now()
print(t2 - t1)
print()

t1 = datetime.now()
# все простые числа в интервале до 1_000_000, содержащие '16'
prime = [x for x in range(3, 1_000_000, 2) if isprime(x) and str(x).count('16') == 1]
print(prime[:100])

def goody(x):
    global prime
    de = ()
    for d in prime:
        if x % d == 0 and x // d in prime:
            de = (d, x // d)
            break
    return de


x = 1_103_285_718
k = 0
while k < 5:
    y = goody(x)
    if y:
        print(x, min(y))
        k += 1
    x += 1
t2 = datetime.now()
print(t2 - t1)

t1 = datetime.now()
# все простые числа в интервале до 1_000_000, содержащие '16'
prime = [x for x in range(3, 1_000_000, 2) if isprime(x) and str(x).count('16') == 1]
print(prime[:100])

ans = set()
for x in prime:
    for y in prime:
        if x <= y:
            if 1_103_285_718 < x * y < 1_200_000_000:
                ans.add((x * y, x))
ans = sorted(ans)
for x, y in ans[:5]:
    print(x, y)
t2 = datetime.now()
print(t2 - t1)