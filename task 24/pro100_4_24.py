'''Текстовый файл содержит строку из символов A, B и C, всего не более чем 10**6 символов.
Найдите максимальную длину строки, состоящей только из комбинаций BAC и СAB.
Например, в строке BABABACCABCABCB такая подстрока BACCABCAB (длина 9).'''

import re
t = open('24-224_NW0S7ra.txt').read().strip()
print(t[:100])

tt = t.replace('CAB', '***').replace('BAC', '***')
pattern = r'[\*]+'
ans = [(len(x), x) for x in re.findall(pattern, tt)]
print(sorted(ans, reverse=True)[:5])