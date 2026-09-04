from itertools import permutations

table = {1: [5,6,7],
         2: [3,8],
         3: [2,4,8],
         4: [3,6,7],
         5: [1,6,8],
         6: [1,4,5],
         7: [1,4],
         8: [2,3,5]}

graph = {'A': set('HED'),
         'B': set('CEF'),
         'C': set('HB'),
         'D': set('AGF'),
         'E': set('AHB'),
         'F': set('DGB'),
         'H': set('AEC'),
         'G': set('DF')}

for p in permutations('ABCDEFGH'):
    temp = {p[k - 1]: set(p[x - 1]  for x in v) for k, v in table.items()}
    if temp == graph:
        print(*p)
