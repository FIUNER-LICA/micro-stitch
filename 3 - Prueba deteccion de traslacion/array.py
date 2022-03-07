import numpy as np

a = np.ndarray((3,4,9))
c = np.array(10)
a.resize(a.shape[0]+10,a.shape[2],a[2][0].size)
print (a.shape)

c = np.zeros_like(a)

print (c.shape)