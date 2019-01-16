def min_of_list_1(alist):
    for i in range(len(alist)):
        for j in range(len(alist)):
            if alist[i] < alist[j]:
                min_num = alist[i]
            else:
                min_num = alist[j]
    return min_num


def min_of_list_2(alist):
    min_num = alist[0]
    for i in range(1, len(alist)):
        if alist[i] < min_num:
            min_num = alist[i]
    return min_num


alist = [1, 2, 3, 4, 5, 2, 3, 45, 76, 8, 9, 4, 3, 0]
print(min_of_list_1(alist))
print(min_of_list_2(alist))
