# 如果 a+b+c=1000，且 a^2+b^2=c^2（a,b,c 为自然数），如何求出所有a、b、c可能的组合?
import time

start_time = time.time()
for i in range(0, 1001):
    for j in range(0, 1001):
        for k in range(0, 1001):
            if i + j + k == 1000 and i * i + j * j == k * k:
                print("i,j,k:%d,%d,%d" % (i, j, k))
end_time = time.time()
print("times:%d" % (end_time - start_time))
print("finished!")
