def shell_sort(list_):
    """希尔排序(不稳定排序)"""
    n = len(list_)
    gap = n // 2
    while gap:
        # 插入算法，与普通的插入算法的区别就是gap步长
        for i in range(gap, n):
            for j in range(i, 0, -1):
                if list_[j] < list_[j - gap]:
                    list_[j], list_[j - gap] = list_[j - gap], list_[j]
                else:
                    break
        gap = gap // 2
    return list_


a = [1, 2, 4, 3, 5, 7, 6, 8, 10, 9, 12, 14, 13, 11, 1, 2, 3]
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 传递a[:]，不会改变a的值
print(shell_sort(a[:]))
# insertion_sort(a[:])
# print(a)
