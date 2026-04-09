'''Напишите программу, которая перебирает целые числа, большие 1326234, в порядке возрастания и ищет среди них числа,
представленные в виде произведения ровно двух простых множителей (не обязательно различных), каждый из которых содержит
в своей записи ровно одну цифру 7.
В ответе в первом столбце таблицы запишите первые 5 найденных чисел в порядке возрастания, а во втором столбце — для
каждого из чисел наибольший из соответствующих им найденных множителей.
'''

def isprime(x):
    for d in range(2, round(x ** 0.5) + 1):
        if x % d == 0:
            return False
    return True


def good(x):
    de = []
    for d in range(2, round(x ** 0.5) + 1):
        if x % d == 0:
            if isprime(d) and isprime(x // d):
                if str(d).count('7') == 1 and str(x // d).count('7') == 1:
                    de.append(d)
                    # if x // d not in de:
                    de.append(x // d)
    de = sorted(de)
    # des = [d for d in de if str(d).count('7')==1]
    if len(de) == 2:
        return de
    return []
    


k = 0
for x in range(1326235, 2000000):
  y = good(x)
  if y:
    k += 1
    print(x, max(y))
    if k == 5:
      break