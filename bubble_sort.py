# def bubble_sort(list_):
#     """这应该也是一种冒泡排序，不同的是此算法每次把最小的元素放到开头"""
#     for i in range(0, len(list_)):
#         for j in range(i + 1, len(list_)):
#             if list_[i] > list_[j]:
#                 list_[i], list_[j] = list_[j], list_[i]
#         print(list_)
#     return list_


def bubble_sort(list_):
    """冒泡排序"""
    for i in range(len(list_) - 1):
        # 外层循环控制循环次数
        for j in range(len(list_) - i - 1):
            # 内层循环控制每一次的循环，每一次循环把最大的数值放到最后
            if list_[j] > list_[j + 1]:
                list_[j], list_[j + 1] = list_[j + 1], list_[j]
    return list_


def bubble_sort_1(list_):
    # 优化1(优化外层循环)
    for i in range(len(list_) - 1):
        # 每次遍历标志位都要先置为0，才能判断后面的元素是否发生了交换
        flag = 0
        # 外层循环控制循环次数
        for j in range(len(list_) - i - 1):
            # 内层循环控制每一次的循环，每一次循环把最大的数值放到最后
            if list_[j] > list_[j + 1]:
                list_[j], list_[j + 1] = list_[j + 1], list_[j]
                flag = 1  # 只要有发生了交换，flag就置为1
        # 判断标志位是否为0，如果为0，说明上面的交换操作没有执行，即后面的元素已经有序，就直接return
        if flag == 0:
            return list_
    return list_


def bubble_sort_2(list_):
    # 优化2(优化内层循环)
    k = len(list_) - 1
    # pos变量用来标记循环里最后一次交换的位置
    pos = 0
    for i in range(len(list_) - 1):
        # 每次遍历标志位都要先置为0，才能判断后面的元素是否发生了交换
        flag = 0
        # 外层循环控制循环次数
        for j in range(k):
            # 内层循环控制每一次的循环，每一次循环把最大的数值放到最后
            if list_[j] > list_[j + 1]:
                list_[j], list_[j + 1] = list_[j + 1], list_[j]
                flag = 1  # 只要有发生了交换，flag就置为1
                pos = j  # 循环里最后一次交换的位置 j赋给pos
        k = pos
        # 判断标志位是否为0，如果为0，说明上面的交换操作没有执行，即后面的元素已经有序，就直接return
        if flag == 0:
            return list_
    return list_


a = [2, 1, 4, 3, 5, 7, 6, 8, 10, 9, 12, 14, 13, 11, 1, 2, 3]
# a = [1, 2, 3, 4, 5, 6]  # 本来就有序的，通过优化1可以使最好时间复杂度达到O(n)
# a = [2, 1, 3, 5, 4, 6, 8, 7, 9, 10, 11, 12]  # 最后几个元素已经有序的，通过优化2可以减少内部循环比较次数
# 传递a[:]，不会改变a的值
print(bubble_sort(a[:]))
print(bubble_sort_1(a[:]))
print(bubble_sort_2(a[:]))
# print(a)
