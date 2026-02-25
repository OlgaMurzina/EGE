'''(№ 2269) Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:
F(n) = n, при n ≤ 3
при n > 3:
  F(n) = F(n–1) + 2*F(n/2), при чётном n;
  F(n) = F(n–1) + F(n-3), при нечётном n;
Определите количество натуральных значений n, при которых F(n) меньше, чем 10**8.'''
from functools import lru_cache
from datetime import datetime


@lru_cache(maxsize=None)
def f(n):
    if n <= 3:
        return n
    if n % 2 == 0:
        return f(n - 1) + 2 * f(n // 2)
    else:
        return f(n - 1) + f(n - 3)
t1 = datetime.now()
ans = []
for n in range(1, 100):
    y = f(n)
    if y < 10 ** 8:
        ans.append(y)
print(len(ans))
t2 = datetime.now()
print(t2 - t1)


t1 = datetime.now()
ff = [0] * 100
for n in range(1, 100):
    if n <= 3:
        ff[n] = n
    else:
        if n % 2 == 0:
            ff[n] = ff[n - 1] + 2 * ff[n // 2]
        else:
            ff[n] = ff[n - 1] + ff[n - 3]
        if ff[n] >= 10 ** 8:
            break
print(n - 1)
t2 = datetime.now()
print(t2 - t1)