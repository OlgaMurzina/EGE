def per(x, q):
    s = ''
    while x > 0:
        s = str(alf[x % q]) + s
        x //= q
    return s

x = 2 * 2187 ** 567 + 729 ** 566 - 2 * 243 ** 565 + 81 ** 564 - 2 * 27 ** 563 - 6561
alf = '0123456789abcdefghijklmnopqrstuvwxyz'
xx = per(x, 27)
print(xx)
a = [y for y in xx if alf.index(y) > 9 and alf.index(y) % 2 == 0]
print(a, len(a))