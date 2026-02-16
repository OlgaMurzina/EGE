'''
В файле электронной таблицы в каждой строке содержатся шесть натуральных чисел. Определите количество строк таблицы, для которых выполнены оба условия:
в строке хотя бы одно число повторяется дважды (ровно 2 раза);
каждое из повторяющихся дважды (ровно 2 раза) чисел превышает каждое неповторяющееся.
'''


data1 = open("/home/dmurzin/Downloads/9.csv").readlines()
data = []
for st in data1:
	s = [int(x) for x in st.split(",")]
	data.append(s)
ans = []
for i in range(len(data)):
	s = data[i]
	a = sorted([s.count(x) for x in set(s)])
	dv = sorted(x for x in s if s.count(x) == 2)
	ost = sorted(x for x in s if s.count(x) == 1)
	if len(dv):
		od = ost + dv
		print(s, a, ost + dv)
		if od == sorted(od):
			print('**', s, a, sorted(od))
			ans.append(s)
		
print(len(ans))
