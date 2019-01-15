def merge_sort(alist):
    """归并排序"""
    n = len(alist)
    if n <= 1:
        return alist
    mid = n // 2
    # left_li 采用归并排序后形成的有序的新的列表
    left_li = merge_sort(alist[:mid])
    # right_li 采用归并排序后形成的有序的新的列表
    right_li = merge_sort(alist[mid:])
    # 将两个有序的子序列合并为一个新的整体
    # merge(left_li,right_li)
    left_pointer, right_pointer = 0, 0
    result = []
    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] <= right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1
    result += left_li[left_pointer:]
    result += right_li[right_pointer:]
    return result


a = [1, 2, 5, 4, 6, 7, 9, 3, 6, 0]
b = merge_sort(a)
print(a)
print(b)
