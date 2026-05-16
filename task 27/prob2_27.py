

def center(cl):
    minn = 10**10
    p = None
    rmin = 10000000000
    rmax = -1000
    for x1, y1 in cl:
        c = 0
        for x2, y2 in cl:
            r = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            c += r
        if c < minn:
            p = (x1, y1)
            minn = c
    x1, y1 = p
    for x2, y2 in cl:
        if x2 != x1 and y2 != y1:
            r = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            rmin = min(rmin, r)
            rmax = max(rmax, r)
    return p, rmin, rmax


data1 = open("/home/dmurzin/Downloads/27_Б.csv").readlines()
data = []
for x in data1:
    s = [float(y) for y in x.split()]
    data.append(s)

cl1 = []
cl2 = []
cl3 = []
for x, y in data:
    if y > 14:
        cl1.append((x, y))
    elif x > 10:
        cl2.append((x, y))
    else:
        cl3.append((x, y))

p1, m1, l1 = center(cl1)
p2, m2, l2 = center(cl2)
p3, m3, l3 = center(cl3)

print("B:", int((m1 + m2 + m3) / 3 * 10000), int((l1 + l2 + l3) / 3 * 10000))