import numpy as np
a = np.arange(1,101,1)
a = a.reshape(10,10)
b = np.square(a)
c = b[b%3==0]
print(c)