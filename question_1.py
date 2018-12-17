# 如果 a+b+c=1000，且 a^2+b^2=c^2（a,b,c 为自然数），如何求出所有a、b、c可能的组合?
for i in range(0, 1000):
    for j in range(0, 1000):
        for k in range(0, 1000):
            if i + j + k == 1000 and i * i + j * j == k * k:
                print(i, j, k)
