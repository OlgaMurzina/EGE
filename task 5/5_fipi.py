"""

"""
ans = []
for n in range(1, 1000):
    nn = bin(n)[2:]
    if nn.count('1') % 2 == 0:
        nn = '10' + nn[2:] + '0'
    else:
        nn = '11' + nn[2:] + '1'
    r = int(nn, 2)
    if r <= 19:
        ans.append(n)
print(max(ans))