"""


"""
from math import dist

def center(cl):
    p = None
    minn = 10 ** 20
    for p1 in cl:
        s = 0
        for p2 in cl:
            s += dist(p1[:-1], p2[:-1])
        if s < minn:
            minn = s
            p = p1
    return p

def max_dist(cl):
    maxx = -10 ** 20
    for p1 in cl:
        for p2 in cl:
            r = dist(p1[:-1], p2[:-1])
            maxx = max(maxx, r)
    return maxx

data1 = open('/home/dmurzin/Downloads/27_A_29357.csv').readlines()
print(data1[:5])
data = []
for s in data1:
    st = s.replace(',', '.').split()
    data.append((float(st[0]), float(st[1]), st[2]))
print(data[:5])

cl1 = []
cl2 = []
for p in data:
    if p[1] > 15:
        cl1.append(p)
    else:
        cl2.append(p)
print(len(cl1), len(cl2), len(data) - len(cl1) - len(cl2))

p1 = center(cl1)
p2 = center(cl2)

kr2 = min([(dist(p2[:-1], x[:-1]), x[0], x[1]) for x in cl2 if 'M' in x[-1] and 'III' in x[-1]])
print(kr2)
ax = kr2[1]
ay = kr2[2]
print('A:', int(ax * 10000), int(ay * 10000))

data1 = open('/home/dmurzin/Downloads/27_B_29357.csv').readlines()
print(data1[:5])
data = []
for s in data1:
    st = s.replace(',', '.').split()
    data.append((float(st[0]), float(st[1]), st[2]))
print(data[:5])

cl1 = []
cl2 = []
cl3 = []
for p in data:
    if p[1] < 30:
        cl1.append(p)
    elif p[0] > 16:
        cl3.append(p)
    else:
        cl2.append(p)
print(len(cl1), len(cl2), len(cl3), len(data) - len(cl1) - len(cl2) - len(cl3))

p1 = center(cl1)
p2 = center(cl2)
p3 = center(cl3)
or1 = [x for x in cl1 if 'K' in x[-1] and 'III' in x[-1]]
or2 = [x for x in cl2 if 'K' in x[-1] and 'III' in x[-1]]
or3 = [x for x in cl3 if 'K' in x[-1] and 'III' in x[-1]]
print(len(or1), len(or2), len(or3))
b1 = dist(p1[:-1], p3[:-1])
jk1 =  [x for x in cl1 if 'G' in x[-1] and 'I' not in x[-1]]
jk2 =  [x for x in cl2 if 'G' in x[-1] and 'I' not in x[-1]]
jk3 =  [x for x in cl3 if 'G' in x[-1] and 'I' not in x[-1]]
mr1 = max_dist(jk1)
mr2 = max_dist(jk2)
mr3 = max_dist(jk3)
b2 = max(mr1, mr2, mr3)
print('B:', int(b1 * 10000), int(b2 * 10000))