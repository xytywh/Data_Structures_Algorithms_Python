import numpy as np


def quick_sort(alist, start, end):
    """快速排序"""
    # 这个判断必须加
    if start >= end:
        return
    # 枢轴，可以随便选，一般选第一个元素
    pivot = alist[start]
    low = start
    high = end
    while low < high:
        while low < high and alist[high] >= pivot:
            high -= 1
        # 这个if判断不加也行
        if low < high:
            alist[low] = alist[high]
            low += 1
        while low < high and alist[low] <= pivot:
            low += 1
        if low < high:
            alist[high] = alist[low]
            high -= 1
    # 从循环退出时，low=high
    alist[low] = pivot
    quick_sort(alist, start, low - 1)
    quick_sort(alist, low + 1, end)


a = np.array([7, 7, 4, 5, 0, 6, 8, 10, 9, 12, 14, 13, 11, 1, 2, 7, 3])
# x的值改变不影响a的值
x = a.copy()
quick_sort(x, 0, len(a) - 1)
print(x)
print(a)
