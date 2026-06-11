from sys import setrecursionlimit

setrecursionlimit(15000)

def g(n):
    if n <= 20:
        return n + 2
    else:
        return g(n - 3) + 1

print(3 * g(37811 - 3) + 7)



g = [0] * 38000
for n in range(37812):
    if n <= 20:
        g[n] = n + 2
    else:
        g[n] = g[n - 3] + 1
f = [0] * 37812
f[37811] = 3 * g[37811 - 3] + 7
print(f[37811])