'''(№ 8183) *(ЕГКР-2025) Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:
F(n) = n при n < 20;
F(n) = (n – 6) · F(n – 7), если n ≥ 20.
Вычислите значение выражения (F(47872) – 290·F(47865)) / F(47858).'''
import sys
from functools import lru_cache


sys.setrecursionlimit(10_000)
@lru_cache(maxsize=None)
def f(n):
    if n < 20:
        return n
    else:
        return (n - 6) * f(n - 7)

print(47866*47859-290*47859)