'''(№ 2276) Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:
F(n) = n*n - 5, при n > 15
F(n) = n*F(n+2) + n + F(n+3), при n ≤ 15
Определите сумму цифр значения F(1).'''

def f(n):
    if n > 15:
        return n * n - 5
    if n <= 15:
        return n * f(n + 2) + n + f(n + 3)

y = f(1)
print(y, sum(int(x) for x in str(y)))

g = [0] * 20
print(g)
for n in range(19, 0, -1):
    if n > 15:
        g[n] = n * n - 5
    else:
        g[n] = n * g[n + 2] + n + g[n + 3]
print(g)
print(g[1], sum(int(x) for x in str(g[1])))