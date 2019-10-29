from collections import deque


def swap_param(L, i, j):
    L[i], L[j] = L[j], L[i]
    return L


# 别人的写法
# def heap_adjust(L, start, end):
#     temp = L[start]
#
#     i = start
#     j = 2 * i
#
#     while j <= end:
#         # 这个表达式是为了让j下标的元素是两个子节点中的较大的
#         if (j < end) and (L[j] < L[j + 1]):
#             j += 1
#         # temp小于其较大的子节点，那么就进行交换，然后再从交换了的那个子节点往下继续判断看需不需要交换
#         if temp < L[j]:
#             L[i] = L[j]
#             i = j
#             j = 2 * i
#         else:
#             break
#     L[i] = temp

# 我自己的写法
def heap_adjust(L, start, end):
    i = start
    j = 2 * i

    while j <= end:
        # 这个表达式是为了让j下标的元素是两个子节点中的较大的
        if (j < end) and (L[j] < L[j + 1]):
            j += 1
        # temp小于其较大的子节点，那么就进行交换，然后再从交换了的那个子节点往下继续判断看需不需要交换
        if L[i] < L[j]:
            L[i], L[j] = L[j], L[i]
            i = j
            j = 2 * i
        else:
            break


def heap_sort(L):
    L_length = len(L) - 1

    first_sort_count = L_length // 2
    for i in range(first_sort_count):
        heap_adjust(L, first_sort_count - i, L_length)
    for i in range(L_length - 1):
        L = swap_param(L, 1, L_length - i)
        heap_adjust(L, 1, L_length - i - 1)

    return [L[i] for i in range(1, len(L))]


if __name__ == '__main__':
    L = deque([50, 16, 30, 10, 60, 90, 2, 80, 70])
    L.appendleft(0)
    print(heap_sort(L))

# def heap_sort(alist):
#     length = len(alist) - 1
#     not_leaf_node = length // 2
#     # 根据alist建一个大根堆(调整每一个非叶节点)
#     # 从最后一个非叶节点开始往上调整
#     for i in range(not_leaf_node):
#         heap_adjust(alist, not_leaf_node - i, length)
#     print(alist[1:], end='\n\n')
#     for i in range(length, 0, -1):
#         # 把第一个结点(最大值)和最后一个结点交换
#         alist[1], alist[i] = alist[i], alist[1]
#         print(alist[1:])
#         # 把最后的已排序好的元素去掉，重新把前面未排序的alist再调整为大根堆
#         # 从最后一个非叶节点开始往上调整，和上面的思路一样
#         for j in range(not_leaf_node):
#             heap_adjust(alist, not_leaf_node - j, i - 1)
#         print(alist[1:], end='\n\n')
#     return alist[1:]
#
#
# def heap_adjust(alist, i, j):
#     # 三个判断是为了让已经排序好的在最后的元素不再进行调整
#     if j < 2 * i:
#         pass
#     elif j == 2 * i:
#         if alist[j] > alist[i]:
#             alist[i], alist[j] = alist[j], alist[i]
#     else:
#         if alist[2 * i] > alist[i] or alist[2 * i + 1] > alist[i]:
#             if alist[2 * i] >= alist[2 * i + 1]:
#                 alist[2 * i], alist[i] = alist[i], alist[2 * i]
#             else:
#                 alist[2 * i + 1], alist[i] = alist[i], alist[2 * i + 1]


# if __name__ == '__main__':
#     alist = [50, 16, 30, 10, 60, 90, 2, 80, 70]
#     alist.insert(0, 0)
#     print(heap_sort(alist))
