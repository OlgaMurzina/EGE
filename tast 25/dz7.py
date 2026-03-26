'''Рассматриваются числа, бо́льшие 700 000, с ровно четырьмя различными делителями. Найдите такие числа,
у которых наименьший и наибольший делители (кроме 1 и самого числа) отличаются не более чем на 15.
В ответе запишите в первом столбце таблицы первые шесть найденных чисел в порядке возрастания,
а во втором — разницу между наименьшим и наибольшим делителями (кроме 1 и самого числа).
'''

def deldig(n):
    r = [1, n]
    for d in range(2, round(n ** 0.5) + 1):
        if n % d == 0:
            if n // d - d > 15:
                return 0
            r.append(d)
            if n // d not in r:
                r.append(n // d)
    r = sorted(r)
    if len(r) == 4:
        return r[-2] - r[1]

from datetime import datetime

t1 = datetime.now()
ans = []
x = 700_000
while len(ans) < 6:
    y = deldig(x)
    if y:
        # print(x, y)
        ans.append((x, y))
    x += 1
for x, y in ans:
    print(x, y)
t2 = datetime.now()
print(t2 - t1)