# def insertion_sort(list_):
#     """插入排序(稳定排序)"""
#     for i in range(1, len(list_)):
#         temp = list_[i]
#         flag = -1
#         for j in range(i - 1, -1, -1):
#             # if list_[i] < list_[j]:
#             if temp < list_[j]:
#                 # 这里一定要用temp进行比较，找了半天bug，唉！
#                 # 因为list[i]值有可能会改变，值有可能变成list[j+1]的值
#                 list_[j + 1] = list_[j]
#                 flag = j
#         if flag != -1:
#             list_[flag] = temp
#         # print(i, flag, list_)
#     return list_


def insertion_sort(list_):
    """插入排序(稳定排序)"""
    # 从第二个位置，即下标为1的元素开始向前插入
    for i in range(1, len(list_)):
        # 从第i个元素开始向前比较，如果小于前一个元素，交换位置
        for j in range(i, 0, -1):
            if list_[j] < list_[j - 1]:
                list_[j], list_[j - 1] = list_[j - 1], list_[j]
            # 加上else，可以使最好时间复杂度为O(n)
            else:
                # 左半部分已经有序了，所以如果无序部分的第一个元素不比
                # 有序部分的最后一个元素小的话，代表此元素已经有序了
                # 可以退出了，不需要再比了
                break
        # print(list_)
    return list_


a = [1, 2, 4, 3, 5, 7, 6, 8, 10, 9, 12, 14, 13, 11, 1, 2, 3]
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 传递a[:]，不会改变a的值
print(insertion_sort(a[:]))
# insertion_sort(a[:])
# print(a)
