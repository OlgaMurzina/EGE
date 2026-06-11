def per(n):
    alf = '0123456789a'
    s = ''
    while n > 0:
        s = alf[n % 11] + s
        n //= 11
    return s

a = 9 * 11 ** 210 + 8 * 11 ** 150
for x in range(3000, 0, -1):
    xx = per(a - x)
    if xx.count('0') == 60:
        print(x)
        break

for x in range(3000, 1, -1):
    s = 9 * 11 ** 210 + 8 * 11 ** 150 - x
    c = 0
    while s > 0:
        if s % 11 == 0:
            c += 1
        s //= 11
    if c == 60:
        print(x)
        break
