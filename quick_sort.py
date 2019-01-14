import numpy as np


def quick_sort(alist, start, end):
    """快速排序"""


a = np.array([1, 2, 4, 3, 5, 7, 6, 8, 10, 9, 12, 14, 13, 11, 1, 2, 3])
# 传递a的拷贝，不会改变a的值
x = a.copy()
quick_sort(x, 0, len(a) - 1)
print(x)
# print(a)
