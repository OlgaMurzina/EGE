from itertools import product 
  
A = sorted("АЭРОБУС") 
  
answer = []
i = 1 
for w in product(A, repeat=5): 
    s = ''.join(w)
    ss = s
    for c in "АЭОБУС": 
        ss = ss.replace(c, '.') 
    if i % 2 == 0 and 'Р.Р' in ss and w.count('У') == 0: 
        answer.append(s)
    i += 1 

print(len(answer))

from itertools import product
import re
  
alf = sorted('АЭРОБУС') 
mask = r'(?:[АЭРОБУС])*Р[^Р]Р(?:[АЭРОБУС])*' 
ans = [] 
for i, s in enumerate(product(alf, repeat=5), 1): 
    sl = ''.join(s) 
    if sl.count('У') == 0 and re.fullmatch(mask, sl) and i % 2 == 0: 
        ans.append(sl) 
print(len(ans)) 
print(set(answer) - set(ans))
