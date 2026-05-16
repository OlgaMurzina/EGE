data1 = open('/home/dmurzin/Downloads/9_29341.csv').readlines()
print(data1[:5])
data = []
for s in data1:
    data.append([int(x) for x in s.split(';')])
print(data[:5])

ans = []
for x in data:
    a = sorted(x)
    if a[-1] < sum(a[:-1]):
        if a[0] + a[-1] != a[1] + a[2]:
            ans.append(x)
print(len(ans))