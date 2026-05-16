def delit(n):
    de = []
    for d in range(2, round(n ** 0.5) + 1):
        if n % d == 0:
            if prost(d):
                if prost(n // d):
                    return n // d
    return 0

def prost(n):
    for d in range(2, round(n ** 0.5) + 1):
        if n % d == 0:
            return False
    if str(n).count("5") == 1:
        return True
    return False

x = 1324728
ans = []
while len(ans) < 5:
    if delit(x):
        ans.append((x, delit(x)))
    x += 1

for x, y in ans:
    print(x, y)