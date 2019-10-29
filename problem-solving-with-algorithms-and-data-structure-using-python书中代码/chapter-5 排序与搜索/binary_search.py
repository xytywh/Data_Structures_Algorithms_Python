# 二分查找适用条件:1.操作的对象必须是有序的 2.支持下表索引(顺序表list)


def binary_search1(alist, item):
    """二分查找，递归1,递归过程中改变的是alist列表本身"""
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
            return binary_search1(alist[:mid], item)
        else:
            return binary_search1(alist[(mid + 1):], item)
    return False


def binary_search2(alist, item, left, right):
    """二分查找，递归2，递归过程中改变的是left和right下标"""
    mid = left + (right - left) // 2
    if left > right:
        return -1
    if alist[mid] == item:
        return mid
    elif alist[mid] > item:
        return binary_search2(alist, item, left, mid - 1)
    else:
        return binary_search2(alist, item, mid + 1, right)


def binary_search3(alist, item):
    """二分查找，非递归，即可以判断元素在不在列表中，也可以返回对应下标"""
    left = 0
    right = len(alist) - 1
    # 怎么确定循环条件，是left和right比，还是left和mid比，还是right和mid比
    # 确定是left和right比之后，那么left能不能等于right呢?
    while left <= right:
        # 第二种写法比第一种写法好的地方在于，防止溢出，例如left和right都是很大的数，不过在python3中，int是long，无需考虑溢出问题
        # mid = (left + right) // 2
        mid = left + (right - left) // 2
        if alist[mid] == item:
            return mid
        elif alist[mid] > item:
            right = mid - 1
        else:
            left = mid + 1
    return -1


alist = [1, 2, 3, 4, 5, 6, 7]
print(binary_search1(alist, 5))
print(binary_search2(alist, 5, 0, len(alist) - 1))
print(binary_search3(alist, 5))
