
def per(x, q):
    alf = '0123456789a'
    s = ''
    while x > 0:
        s = alf[x % q] + s
        x //= q
    return s

a = 9 * 11 ** 210 + 8 * 11 ** 150
for x in range(1, 3001):
    xx = per(a - x, 11)
    if xx.count('0') == 60:
        print(x)
