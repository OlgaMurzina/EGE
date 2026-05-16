def center(cl):
    dot = []
    s = 10 ** 10
    for x1, y1 in cl:
        k = 0
        for x2, y2 in cl:
            k += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        if k < s:
            s = k
            dot = [x1, y1]
    return dot

def kol(cl, ctr):
    k = 0
    for x, y in cl:
        if x == ctr[0] and y == ctr[1]:
            continue
        if ((x - ctr[0]) ** 2 + (y - ctr[1]) ** 2) ** 0.5 <= 0.4:
            k += 1
    return k

def dist(cl, ctr):
    mx = - 10 ** 10
    for x, y in cl:
        if ((x - ctr[0]) ** 2 + (y - ctr[1]) ** 2) ** 0.5 > mx:
            mx = ((x - ctr[0]) ** 2 + (y - ctr[1]) ** 2) ** 0.5
    return mx

f = open('27_А_pr.csv').readlines()
d = []
for s in f:
    d.append(list(map(float, s[:-1].split(' '))))
cl1 = []
cl2 = []
for x, y in d:
    if x > 10:
        cl1.append((x, y))
    else:
        cl2.append((x, y))

ctr1 = center(cl1)
ctr2 = center(cl2)
print(min(len(cl1), len(cl2)), int((((ctr1[0] - 8) ** 2 + (ctr1[1] - 4.5) ** 2) ** 0.5 + ((ctr2[0] - 8) ** 2 + (ctr2[1] - 4.5) ** 2) ** 0.5) * 10000))


f = open('27_Б_pr.csv').readlines()
d = []
for s in f:
    d.append(list(map(float, s[:-1].split(' '))))
cl1 = []
cl2 = []
cl3 = []
for x, y in d:
    if 15 < y < 25 and 0 < x < 10:
        cl1.append((x, y))
    elif y < 15 and 5 < x < 15:
        cl2.append((x, y))
    elif 30 < y and 15 < x:
        cl3.append((x, y))
cl = sorted([cl1, cl2, cl3], key=len)
ctrmin = center(cl[0])
ctrsr = center(cl[1])
k = kol(cl[0], ctrmin)
ans = dist(cl[1], ctrsr)
print(k, int(ans * 10000))
