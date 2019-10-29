# 计数排序
def counting_sort(alist):  # k = max(a)
    n = len(alist)  # 计算a序列的长度
    out = [0 for _ in range(n)]  # 设置输出序列并初始化为0
    counting_list = [0 for _ in range(max(alist) + 1)]  # 设置计数序列并初始化为0，
    # 统计alist中每个元素出现的次数，例如counting_list[3]=4，代表在alist中3出现了4次
    for elem in alist:
        counting_list[elem] = counting_list[elem] + 1
    print(counting_list)
    # 对于每一个元素i，统计小于等于i的元素个数，例如，counting_list[2]=10，代表小于等于2的元素共有10个
    for i in range(1, len(counting_list)):
        counting_list[i] += counting_list[i - 1]
    print(counting_list)
    for elem in alist:
        # 注意elem对应的下标要减1，例如，counting_list[2]=10
        # 那么元素2在新的数组out中占据的位置是[10-alist.count(2),9]，即2-9
        out[counting_list[elem] - 1] = elem
        counting_list[elem] = counting_list[elem] - 1
    return out


alist = [2, 2, 3, 8, 7, 1, 2, 2, 2, 7, 3, 9, 8, 2, 1, 4, 2, 4, 6, 9, 2]
print(counting_sort(alist))
