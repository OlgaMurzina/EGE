'''


'''

def center(cl):
    minn = 10 ** 20
    p = None
    for x1, y1 in cl:
        s = 0
        for x2, y2 in cl:
            r = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            s += r
        if s < minn:
            minn = s
            p = (x1, y1)
    return p


data1 = open('27_A_28946.csv').readlines()
print(data1[:10])
data = []
for s in data1:
    data.append([float(x) for x in s.replace(',', '.').split()])
print(data[:10])

cl1 = []
cl2 = []
for x, y in data:
    if y > 15:
        cl1.append((x, y))
    else:
        cl2.append((x, y))
print(len(cl1), len(cl2), len(data) - (len(cl1) + len(cl2)))

x1, y1 = center(cl1)
x2, y2 = center(cl2)
a1 = 0
for x, y in cl1:
    if y < y1:
        a1 += 1
a2 = abs(x2 - x1)
print('A:', a1, int(a2 * 10000))

data1 = open('/home/dmurzin/Downloads/27_B_28946.csv').readlines()
print(data1[:10])
data = []
for s in data1:
    data.append([float(x) for x in s.replace(',', '.').split()])
print(data[:10])

cl1 = []
cl2 = []
cl3 = []
for x, y in data:
    if y > 22:
        cl1.append((x, y))
    elif x > 24:
        cl3.append((x, y))
    else:
        cl2.append((x, y))
print(len(cl1), len(cl2), len(cl3), len(data) - (len(cl1) + len(cl2) + len(cl3)))

x1, y1 = center(cl1)
x2, y2 = center(cl2)
x3, y3 = center(cl3)
b1 = 0
for x, y in cl3:
    if x3 - 0.9 <= x <= x3 + 0.9 and y3 - 0.9 <= y <= y3 + 0.9:
        b1 += 1
b2 = abs(y2 - y1)
print('B:', b1, int(b2 * 10000))
