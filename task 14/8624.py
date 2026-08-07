'''(№ 8624) Значение арифметического выражения 75**314 + 75**118 – х, где х – натуральное число, не превышающее 32000,
записали в 75-ричной системе счисления. Определите минимальное возможное количество нулей в 75-ричной записи числа,
являющегося значением данного арифметического выражения. В ответе запишите только целое число.'''

def conv(n: int, q: int) -> list:
    if n == 0:
        return [0]
    s = []
    while n > 0:
        s = [n % q] + s
        n //= q
    return s

def conv_v2(n: int, q: int) -> int:
    if n == 0:
        return 1
    nl_cnt = 0
    while n > 0:
        nl_cnt += 1 if n % q == 0 else 0
        n //= q
    return nl_cnt

from datetime import datetime

t1 = datetime.now()
ans = []
num = 75 ** 314 + 75 ** 118
for x in range(1, 32000):
    n = num - x
    nn = conv(n, 75)
    ans.append(nn.count(0))
print(min(ans))
t2 = datetime.now()
print(t2 - t1)


t1 = datetime.now()
num = 75 ** 314 + 75 ** 118
minn = 100000
for x in range(1, 32000):
    n = num - x
    nn = conv(n, 75)
    minn = min(minn, nn.count(0))
print(minn)
t2 = datetime.now()
print(t2 - t1)

t1 = datetime.now()
num = 75 ** 314 + 75 ** 118
minn = 100000
for x in range(1, 32000):
    n = num - x
    nn = conv_v2(n, 75)
    minn = min(minn, nn)
print(minn)
t2 = datetime.now()
print(t2 - t1)

t1 = datetime.now()
num = 75 ** 314 + 75 ** 118
minn = 100000
for x in range(1, 32000):
    n = num - x
    k = 0
    while n > 0:
        k += 1 if n % 75 == 0 else 0
        n //= 75
    minn = min(minn, k)
print(minn)
t2 = datetime.now()
print(t2 - t1)