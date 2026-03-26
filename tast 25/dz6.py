'''
Пусть R — сумма различных натуральных делителей целого числа, не считая единицы и самого числа.
Если таких делителей у числа нет, значение R принимается равным нулю.
Напишите программу, которая перебирает целые числа больше 1 500 000 в порядке возрастания и
ищет среди них такие, для которых R — простое число.
В ответе запишите в первом столбце таблицы первые пять найденных чисел в порядке возрастания,
а во втором — соответствующие им значения R.
Например, для числа 20 R = 2 + 4 + 5 + 10 = 21.
Количество строк в таблице для ответа избыточно.
'''

def is_prime(n):
    for d in range(2, round(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True

def deldig(n):
    r = []
    for d in range(2, round(n ** 0.5) + 1):
        if n % d == 0:
            r.append(d)
            if n // d not in r:
                r.append(n // d)
    if r:
        return sum(r)
    return 0

from datetime import datetime

t1 = datetime.now()
ans = []
x = 1_500_000
while len(ans) < 5:
    y = deldig(x)
    if y:
        z = is_prime(y)
        if z:
            ans.append((x, y))
    x += 1
print(*ans, sep='\n')
t2 = datetime.now()
print(t2 -t1)

t1 = datetime.now()
ans = []
x = 1_500_000
for x in range(1500000, 100000000):
    y = deldig(x)
    if y:
        z = is_prime(y)
        if z:
            ans.append((x, y))
    if len(ans) == 5:
        break
print(*ans, sep='\n')
t2 = datetime.now()
print(t2 -t1)

