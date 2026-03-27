def diametr(cl1, cl2):
    maxx = -10 ** 20
    p1 = None
    p2 = None
    for x1, y1 in cl1:
        for x2, y2 in cl2:
            r = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            if r > maxx:
                maxx = r
                p1 = (x1, y1)
                p2 = (x2, y2)
    return maxx, p1, p2


data1 = open('27_A_mart_2026.txt').readlines()
# print(data1[:5])
data = []
for s in data1:
    data.append([float(x) for x in s.split()])
# print(data[:5])

cl1 = []
cl2 = []
for x, y in data:
    if x > 0:
        cl1.append((x, y))
    else:
        cl2.append((x, y))
# print(len(cl1), len(cl2), len(data))

d, p1, p2 = diametr(cl1, cl2)
print('A:', int(abs(p1[0] - p2[0]) * 1000), int((p1[1] + p2[1]) * 1000))

data1 = open('27_B_mart_2026.txt').readlines()
# print(data1[:5])
data = []
for s in data1:
    data.append([float(x) for x in s.split()])
# print(data[:5])

cl1 = []
cl2 = []
cl3 = []
for x, y in data:
    if 1 < x < 9:
        cl1.append((x, y))
    elif -14.5 < x < -1:
        if y > 0:
            cl2.append((x, y))
        else:
            cl3.append((x, y))
# print(len(cl1), len(cl2), len(cl3), len(data) - (len(cl1) + len(cl2) + len(cl3)))
d12, p12, p21 = diametr(cl1, cl2)
d23, p23, p32 = diametr(cl2, cl3)
d13, p13, p31 = diametr(cl1, cl3)
q1 = d12 + d23 + d13
maxx = -10 ** 20
for x, y in [p12, p21, p23, p32, p13, p31]:
    d = ((1 - x) ** 2 + (1 - y) ** 2) ** 0.5
    if d > maxx:
        maxx = d
q2 = maxx
print('B', int(q1 * 100), int(q2 * 100))
