import time
print("按下回车开始计时，按下ctrl+c停止计时。")

import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(a)

import time
a = np.random.rand(1000000)
b = np.random.rand(1000000)

tic = time.time()
c = np.dot(a, b)
toc = time.time()
print(c)
print("vectorized version " + str(1000*(toc - tic)) + "ms")

c = 0
tic = time.time()
for i in range(1000000):
    c += a[i] * b[i]

toc = time.time()
print(c)
print("forloop version " + str(1000*(toc - tic)) + "ms")





