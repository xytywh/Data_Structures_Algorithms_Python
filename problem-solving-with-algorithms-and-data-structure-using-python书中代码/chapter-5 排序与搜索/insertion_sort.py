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


# def insertion_sort(list_):
#     """插入排序(稳定排序)"""
#     # 从第二个位置，即下标为1的元素开始向前插入
#     for i in range(1, len(list_)):
#         # 从第i个元素开始向前比较，如果小于前一个元素，交换位置
#         for j in range(i, 0, -1):
#             if  < list_[j - 1]:
#                 list_[j], list_[j - 1] = list_[j - 1], list_[j]
#             # 加上else，可以使最好时间复杂度为O(n)
#             else:
#                 # 左半部分已经有序了，所以如果无序部分的第一个元素不比
#                 # 有序部分的最后一个元素小的话，代表此元素已经有序了
#                 # 可以退出了，不需要再比了
#                 break
#         # print(list_)
#     return list_

# 我自己的实现
def insertion_sort(list_):
    for i in range(1, len(list_)):
        temp = list_[i]
        flag = False
        j = i - 1
        for j in range(i - 1, -1, -1):
            # 把前面有序的部分往后移动，空出的位置就是当前元素要插入的位置
            if temp < list_[j]:
                flag = True
                list_[j + 1] = list_[j]
            else:
                break
        # 只有当循环里面发生移动的时候，才插到当前位置，否则，代表当前元素位置是对的
        if flag:
            list_[j] = temp
    return list_


if __name__ == '__main__':
    a = [6, 7, 8, 9, 4, 3, 2, 5, 6, 7, 8, 4, 3, 2, 1, 12, 5, 7, 9, 6, 4, 6]
    # a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # 传递a[:]，不会改变a的值
    print(insertion_sort(a[:]))
    # insertion_sort(a[:])
    # print(a)
