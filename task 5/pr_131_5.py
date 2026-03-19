'''

'''

def per(n: int, q: int) -> str:
    if n == 0:
        return '0'
    alf = '0123456789abcdefghijklmnopqrstuvwxyz'
    s = ''
    while n > 0:
        s = alf[n % q] + s
        n //= q
    return s


minn = 10 ** 10
z = 'a'
for n in range(1, 1000):
    n_3 = per(n, 3)
    if n % 3 == 0:
        n_3 = n_3 + n_3[-2:]
    else:
        # s = 1 * n_3.count('1') + 2 * n_3.count('2')   # 1022 -> 1 + 2 + 2 = 1 * 1 + 2 * 2 = 5
        s = sum(int(x) for x in n_3) * 3
        n_3 = n_3 + per(s, 3)
    r = int(n_3, 3)
    if abs(r - 826) < minn:
        minn = abs(r - 826)
        z = r
        print(minn, r)
print(z)
