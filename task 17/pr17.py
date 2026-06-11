t = [int(x) for x in open('17-04-1.txt').readlines()]
print(t[:100])

max7 = max([x for x in t if x % 7 == 0])
print(max7)

k = 0
maxx = -10 ** 6
for i in range(len(t) - 1):
    if t[i] % 10 == max7 % 10 and t[i + 1] % 10 == max7 % 10:
        k += 1
        s = t[i] + t[i + 1]
        maxx = max(maxx, s)
print(k, maxx)