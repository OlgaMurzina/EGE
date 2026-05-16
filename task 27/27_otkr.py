from math import  *

def center(cl):
    p = None
    minn = 10 ** 20
    for x1, y1, t1 in cl:
        s = 0
        for x2, y2, t2 in cl:
            s += dist((x1, y1), (x2, y2))
        if s < minn:
            minn = s
            p = (x1, y1)
    return p

def dist_max(cl):
    maxx = -10 ** 20
    for x1, y1, t1 in cl:
        for x2, y2, t2 in cl:
            r = dist((x1, y1), (x2, y2))
            if r > maxx:
                maxx = r
    return maxx

data1 = open('/home/dmurzin/Downloads/27_A_29357.csv').readlines()
print(data1[:5])
data = []
for s in data1:
    st = s.replace(',', '.').split()
    data.append([float(st[0]), float(st[1]), st[-1]])
print(data[:5])

# A
cl1 = []
cl2 = []
for x, y, t in data:
    if y > 15:
        cl1.append((x, y, t))
    else:
        cl2.append((x, y, t))
print(len(cl1), len(cl2), len(data) - len(cl1) - len(cl2))

p1 = center(cl1)
p2 = center(cl2)

a1 = min([(dist(p2, x[:-1]), x[0], x[1]) for x in cl2 if 'M' in x[-1] and 'III' in x[-1]])
print('A:', int(a1[1] * 10000), int(a1[2] * 10000))

data1 = open('/home/dmurzin/Downloads/27_B_29357.csv').readlines()
print(data1[:5])
data = []
for s in data1:
    st = s.replace(',', '.').split()
    data.append([float(st[0]), float(st[1]), st[-1]])
print(data[:5])

# B
cl1 = []
cl2 = []
cl3 = []
for x, y, t in data:
    if y < 30:
        cl1.append((x, y, t))
    elif x > 16:
        cl3.append((x, y, t))
    else:
        cl2.append((x, y, t))
print(len(cl1), len(cl2), len(cl3), len(data) - len(cl1) - len(cl2) - len(cl3))

p1 = center(cl1)
p2 = center(cl2)
p3 = center(cl3)

og1 = [x for x in cl1 if 'K' in x[-1] and 'III' in x[-1]]
og2 = [x for x in cl2 if 'K' in x[-1] and 'III' in x[-1]]
og3 = [x for x in cl3 if 'K' in x[-1] and 'III' in x[-1]]
print(len(og1), len(og2), len(og3))
b1 = dist(p1, p3)

yk1 = [x for x in cl1 if 'G' in x[-1] and 'I' not in x[-1]]
yk2 = [x for x in cl2 if 'G' in x[-1] and 'I' not in x[-1]]
yk3 = [x for x in cl3 if 'G' in x[-1] and 'I' not in x[-1]]
print(yk1)
max1 = dist_max(yk1)
max2 = dist_max(yk2)
max3 = dist_max(yk3)
b2 = max(max1, max2, max3)
print('B:', int(b1 * 10000), int(b2 * 10000))