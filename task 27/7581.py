'''

'''

def center(cl):
    p = None
    minn = 10 ** 20
    for x1, y1 in cl:
        s = 0
        for x2, y2 in cl:
            s += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        if s < minn:
            minn = s
            p = (x1, y1)
    return p

# A
data1 = open('/home/dmurzin/Downloads/27-p00a.csv').readlines()
data = []
for s in data1:
    data.append([float(x) for x in s.replace(',', '.').split('\t')])
print(data[:5])

cl1 = []
cl2 = []
for x, y in data:
    if y < 3:
        cl1.append((x, y))
    else:

        cl2.append((x, y))
print(len(cl1), len(cl2), len(data) - (len(cl1) + len(cl2)))

x1, y1 = center(cl1)
x2, y2 = center(cl2)
px = (x1 + x2) / 2
py = (y1 + y2) / 2
print('A:', int(px * 10000), int(py * 10000))

# B
data1 = open('/home/dmurzin/Downloads/27-p00b.csv').readlines()
data = []
for s in data1:
    data.append([float(x) for x in s.replace(',', '.').split('\t')])
print(data[:5])

cl1 = []
cl2 = []
cl3 = []
for x, y in data:
    if y < 3:
        cl1.append((x, y))
    elif y > 7:
        cl3.append((x, y))
    else:
        cl2.append((x, y))
print(len(cl1), len(cl2), len(cl3), len(data) - (len(cl1) + len(cl2) + len(cl3)))

x1, y1 = center(cl1)
x2, y2 = center(cl2)
x3, y3 = center(cl3)
px = (x1 + x2 + x3) / 3
py = (y1 + y2 + y3) / 3
print('B:', int(px * 10000), int(py * 10000))