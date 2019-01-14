import sys


# sys.setrecursionlimit(100000000)  # 设置允许的递归次数

# 我的解法，显然比下面的解法好多了，大大减少了递归的次数，大大减少了执行时间
def find_change(alist, money):
    """

    :param alist: 是一个包含可能零钱取值的list
    :param money: 是总钱数
    :return: int 最小的组成可能
    """
    if money in alist:
        return 1
    else:
        if money >= 25:
            # 贪心法，肯定先从最大的开始找
            return find_change(alist, money % 25) + money // 25
        elif money >= 10:
            return find_change(alist, money % 10) + money // 10
        elif money >= 5:
            return find_change(alist, money % 5) + money // 5
        else:
            return money


# 书上的解法
def find_change(coinvaluelist, change):
    mincoins = change
    if change in coinvaluelist:
        return 1
    else:
        for i in [c for c in coinvaluelist if c <= change]:
            numcoins = 1 + find_change(coinvaluelist, change - i)
        if numcoins < mincoins:
            mincoins = numcoins
    return mincoins


print(find_change([1, 5, 10, 25], 63))
