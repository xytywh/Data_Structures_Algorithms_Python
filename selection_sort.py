def selection_sort(list_):
    """选择排序(不稳定排序)"""
    for i in range(len(list_) - 1):
        for j in range(i + 1, len(list_)):
            if list_[i] > list_[j]:
                list_[i], list_[j] = list_[j], list_[i]
        # print(list_)
    return list_


# def selection_sort(list_):
#     """选择排序(不稳定排序)"""
#     for i in range(len(list_) - 1):
#         for j in range(len(list_) - 1, i, -1):
#             if list_[j] < list_[j - 1]:
#                 list_[j - 1], list_[j] = list_[j], list_[j - 1]
#         print(list_)
#     return list_


a = [1, 2, 4, 3, 5, 7, 6, 8, 10, 9, 12, 14, 13, 11, 1, 2, 3]
# 传递a[:]，不会改变a的值
print(selection_sort(a[:]))
# print(a)
