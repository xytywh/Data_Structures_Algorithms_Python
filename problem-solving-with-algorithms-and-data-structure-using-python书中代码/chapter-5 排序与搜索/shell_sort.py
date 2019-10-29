def shell_sort(list_):
    """希尔排序(不稳定排序)"""
    n = len(list_)
    # 我们这里gap的取值是一开始取整个数组长度的一半，然后在循环遍历的过程中，每次长度减半
    # 最后一次遍历的时候，gap为1，相当于还需要对整个数组从起始到结尾进行判断

    # 最优时间复杂度取决于gap的取值，需要严密的数学计算
    gap = n // 2
    while gap:
        # 插入算法，与普通的插入算法的区别就是gap步长
        for i in range(gap, n):
            # for j in range(i, 0, -1):
            for j in range(i, 0, -gap):
                if list_[j] < list_[j - gap]:
                    list_[j], list_[j - gap] = list_[j - gap], list_[j]
                else:
                    break
        # 缩短gap步长
        gap = gap // 2
    return list_


a = [1, 2, 4, 3, 5, 7, 6, 8, 10, 9, 12, 14, 13, 11, 1, 2, 3, 3, 2, 1, 4, 5, 3, 2, 5, 6, 7, 9]
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 传递a[:]，不会改变a的值
print(shell_sort(a[:]))
# insertion_sort(a[:])
# print(a)
