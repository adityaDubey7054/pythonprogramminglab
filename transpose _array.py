import numpy as np
r,c = map(int,input().split())
m = []
for in in range(r):
	a = list(map(int,input().split()))
	m.append(a)
	arr = np.array(m)
	out1 = m.transpose()
	out2 = m.flatter()
print(out1)
print(out2)