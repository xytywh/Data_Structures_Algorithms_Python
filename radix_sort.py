# 基数排序
"""基数排序适用于：
(1)数据范围较小，建议在小于1000
(2)每个数值都要大于等于0"""


def radix_sort(alist, maxdigit):
    """
    :param alist:
    :param maxdigit: 最大数据位数
    :return:
    """
    for i in range(maxdigit):  # maxdigit轮排序
        s = [[] for _ in range(10)]  # 因每一位数字都是0~9，建10个桶
        for elem in alist:
            # 从每个元素的最低位开始进行排序
            s[elem // (10 ** i) % 10].append(elem)
        alist = [a for b in s for a in b]
        print(alist)
    return alist


alist = [3, 447, 318, 15, 47, 125, 36, 264, 275, 32, 46, 4, 149, 50, 48]
print(radix_sort(alist, 3))
