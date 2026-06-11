a = [int(x) for x in open('26-j1.txt').readlines()[1:]]
data =  {}
for x in a:
    data[x] = data.get(x, 0) + 1 
print(data)
s = 0
ans = []
for k in data.keys():
    if k not in ans and 100 - k not in ans and 100 - k in data.keys():
        if k != 50:
            ans.append(k)
            ans.append(100 - k)
            s += min(data[k], data[100-k])
        else:
            s += data[k] // 2
print(s)