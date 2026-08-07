'''(№ 7841) *В числах BA3x98ADF(153) и C1x78A75(153) переменная x обозначает некоторую цифру из алфавита системы
счисления с основанием 153. Определите наибольшее значение x, при котором произведение приведённых чисел кратно 152.
В ответе запишите значение числа 5xA(153) в десятичной системе счисления.'''

def my_int(n: list, q: int) -> int:
    nn = n[::-1]
    s = 0
    for i in range(len(nn)):
        s += nn[i] * q ** i
    return s


alf = '0123456789abcdefghijklmnopqrstuvwxyz'.upper()
for x in range(153):
    a = my_int([alf.index(y) if y != 'x' else x for y in f'BA3x98ADF'], 153)
    b = my_int([alf.index(y) if y != 'x' else x for y in f'C1x78A75'], 153)
    if a * b % 152 == 0:
        print(x, my_int([alf.index(y) if y != 'x' else x for y in f'5xA'], 153))

