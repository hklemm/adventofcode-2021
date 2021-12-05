import numpy as np

a = np.loadtxt('input.txt')
b = a[1:] - a[:-1]
c = b>0
print('The first solution is:', np.sum(c.astype(int)))

d = a[:-2] + a[1:-1] + a[2:]
e = d[1:] - d[:-1]
f = e>0
print('The second solution is:', np.sum(f.astype(int)))
