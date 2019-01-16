# 二分查找适用条件:1.操作的对象必须是有序的 2.支持下表索引(顺序表list)


def binary_search(alist, item):
    """二分查找，递归"""
    # left = 0
    # right = len(alist) - 1
    # mid = (left + right) // 2
    # if alist[mid] == item:
    #     return mid
    # elif alist[mid] > item:
    #     binary_search(alist[0:mid], item)
    # else:
    #     binary_search(alist[(mid + 1):], item)
    # return -1
    # 下面的做法用于查找某个元素在不在某个有序列表中，可以
    # 但是如果还想返回下标就不行了，因为每次递归时使用的列表变了
    n = len(alist)
    # 必须要加判断，否则，当元素不在有序列表中时，下面代码继续执行，会导致list index out of range
    if n > 0:
        mid = n // 2
        if alist[mid] == item:
            return True
        elif alist[mid] > item:
            # 下面必须是 return某个值,想一想不return，会有什么不同
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[(mid + 1):], item)
    return False


def binary_search(alist, item):
    """二分查找，非递归，即可以判断元素在不在列表中，也可以返回对应下标"""
    left = 0
    right = len(alist) - 1
    # 怎么确定循环条件，是left和right比，还是left和mid比，还是right和mid比
    # 确定是left和right比之后，那么left能不能等于right呢?
    while left <= right:
        mid = (left + right) // 2
        if alist[mid] == item:
            return mid
        elif alist[mid] > item:
            right = mid - 1
        else:
            left = mid + 1
    return -1


alist = [1, 2, 3, 4, 5, 6, 7]
print(binary_search(alist, 5))
