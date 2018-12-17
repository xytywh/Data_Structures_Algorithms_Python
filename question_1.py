for i in range(0, 1000):
    for j in range(0, 1000):
        for k in range(1000 - i - j, 1000):
            if i + j + k == 1000 and i * i + j * j == k * k:
                print(i, j, k)
