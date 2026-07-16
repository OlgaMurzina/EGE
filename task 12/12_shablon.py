'''Реализация машины Тьюринга как есть, плюс анализ на небольшой строке - от PRO100'''

from itertools import product

res = []
# подготовка всех возможных вариантов входной строки на небольшой длине
for p in product(['0', '1'], repeat=10):
    # подготовка входной строки в виде списка(!), т.к. только в нем можно менять элементы при обращении по индексу
    lenta = [' '] + list(p) + [' ']
    # реализация МТ в соответствие с условием задачи
    lenta_start = list(lenta)   # начальная строка
    q = 0    # начальное состояние q0
    cur_index = 11   # начальное положение каретки
    # имитация бесконечной ленты
    while True:
        if q == 0:   # q0
            if lenta[cur_index] == ' ':
                lenta[cur_index] = ' '   # замена
                cur_index -= 1    # сдвиг каретки
                q = 1    # смена состояния
        elif q == 1:   # q1
            if lenta[cur_index] == ' ':
                lenta[cur_index] = ' '  # замена
                break    # stop
            elif lenta[cur_index] == '1':
                lenta[cur_index] = '0'   # замена
                break   # стоп
            elif lenta[cur_index] == '0':
                lenta[cur_index] = '1'   # замена
                cur_index -= 1   # сдвиг каретки
                q = 1   # смена состояния
    # подготовка вывода данных для визуального анализа - что пришло, что полуилось
    lenta_start = ''.join(lenta_start).strip()
    lenta = ''.join(lenta).strip()
    print(lenta_start, lenta)


    # шаблон через строку для МТ:
    # реализация через строку - для направления справа налево нужно делать разворот строки и изменять сдвиг каретки
tabl = {0: {' ': ['*', 1, 1]},
        1: {' ': ['1', 1, 2],
            '0': ['1', 0, 1],
            '1': ['0', 1, 1]},
        2: {' ': ['*', 0, 2]}
        }

st = (' ' + bin(2047)[2:] + ' ')[::-1]
print(st)
print()
q = 0
i = 0
while i < len(st):
    symb = st[i]
    st = st.replace(st[i], tabl[q][symb][0], 1)
    if tabl[q][symb][1] == 0:
        break
    i += tabl[q][symb][1]
    q = tabl[q][symb][2]
    print(st)
print()
st = st.replace('*', '')[::-1]
print(st)

