"""


"""
# чтение файла
s = open('/home/dmurzin/Downloads/24_29354.txt').read()
print(s[:100])
# MAX
bc = [-1] + [i for i in range(len(s) - 1) if s[i:i+2] == 'BC'] + [len(s)]
print(bc[:50])
bcc = zip(bc, bc[191:])
maxx = -10 ** 6
for i1, i2 in bcc:
    maxx = max(maxx, i2 - i1)
print(maxx)

max_s = -10 ** 6
for i in range(len(bc) - 191):
    max_s = max(len(s[bc[i] + 1: bc[i + 191]]) + 1, max_s)
print(max_s)