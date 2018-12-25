def bubble_sort(list):
    for i in range(0, len(list)):
        for j in range(i + 1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list


a = [1, 2, 4, 3, 5, 7, 6, 8, 10, 9, 12, 14, 13, 11, 1, 2, 3]
# 传递a[:]，不会改变a的值
print(bubble_sort(a[:]))
print(a)

