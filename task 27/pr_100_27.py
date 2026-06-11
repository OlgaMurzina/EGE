from math import *

def center(cl):
    p = None
    minn = 10 ** 20
    for p1 in cl:
        s = 0
        for p2 in cl:
            s += dist(p1[:-1], p2[:-1])
        if s < minn:
            p = p1
            minn = s
    return p


data1 = open('27-120a (Copy).csv').readlines()
data = []
for x in data1:
    y = x.replace(',', '.').split('\t')
    data.append([float(y[0]), float(y[1]), y[2].strip()])
# print(data[:10])

cl1 = []
cl2 = []
for x, y, t in data:
    if y > 8:
        cl1.append((x, y, t))
    else:
        cl2.append((x, y, t))
# print(len(cl1), len(cl2), len(data) - len(cl1) - len(cl2))

p1 = center(cl1)
p2 = center(cl2)
bel51 = [x for x in cl1 if 'G' in x[-1] and '5' in x[-1]]
# print(bel51)
bel52 = [x for x in cl2 if 'G' in x[-1] and '5' in x[-1]]
# print(bel52)
a1 = p2[0]
a2 = p1[1]
print(int(a1 * 10000), int(a2 * 10000))


data1 = open('27-120b (Copy).csv').readlines()
data = []
for x in data1:
    y = x.replace(',', '.').split('\t')
    data.append([float(y[0]), float(y[1]), y[2].strip()])
# print(data[:10])

cl1 = []
cl2 = []
cl3 = []
for x, y, t in data:
    if y > 22:
        cl1.append((x, y, t))
    elif y > 16:
        cl3.append((x, y, t))
    else:
        cl2.append((x, y, t))
# print(len(cl1), len(cl2), len(cl3), len(data) - len(cl1) - len(cl2) - len(cl3))

p1 = center(cl1)
p2 = center(cl2)
p3 = center(cl3)
yrg1 = [x for x in cl1 if 'II' in x[-1] and 'V' not in x[-1] and 'III' not in x[-1]]
# print(yrg1)
yrg2 = [x for x in cl2 if 'II' in x[-1] and 'V' not in x[-1] and 'III' not in x[-1]]
# print(yrg2)
yrg3 = [x for x in cl3 if 'II' in x[-1] and 'V' not in x[-1] and 'III' not in x[-1]]
# print(yrg3)
b1 = sum([dist(p2[:-1], x[:-1]) for x in yrg2]) / len(yrg2)
b2 = sum([dist(p1[:-1], x[:-1]) for x in yrg1]) / len(yrg1)
print(int(b1 * 10000), int(b2 * 10000))
