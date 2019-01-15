import sys

sys.setrecursionlimit(100000000)  # 设置允许的递归次数


# 我的解法，显然比下面的解法好多了，大大减少了递归的次数，大大减少了执行时间
def find_change_1(alist, money):
    """

    :param alist: 是一个包含可能零钱取值的list
    :param money: 是总钱数
    :return: int 最小的组成可能
    """
    if money in alist:
        return 1
    else:
        if money >= 25:
            # 贪心法，肯定先从最大的开始找,但并不是每次 贪心都可以找到最优解
            return find_change_1(alist, money % 25) + money // 25
        elif money >= 10:
            return find_change_1(alist, money % 10) + money // 10
        elif money >= 5:
            return find_change_1(alist, money % 5) + money // 5
        else:
            return money


# 书上的解法
def find_change_2(coinvaluelist, change):
    mincoins = change
    if change in coinvaluelist:
        return 1
    else:
        for i in [c for c in coinvaluelist if c <= change]:
            numcoins = 1 + find_change_2(coinvaluelist, change - i)
            if numcoins < mincoins:
                mincoins = numcoins
    return mincoins


# 使用称为"函数值缓存"的方法提升程序性能
def find_change_3(coinvaluelist, change, knowresults):
    mincoins = change
    if change in coinvaluelist:
        knowresults[change] = 1
        return 1
    elif knowresults[change] > 0:
        return knowresults[change]
    else:
        for i in [c for c in coinvaluelist if c <= change]:
            numcoins = 1 + find_change_3(coinvaluelist, change - i, knowresults)
            if numcoins < mincoins:
                mincoins = numcoins
                knowresults[change] = mincoins
    return mincoins


# 动态规划
def find_change_4(coinvaluelist, change, knowresults):
    mincoins = change
    if change in coinvaluelist:
        knowresults[change] = 1
        return 1
    elif knowresults[change] > 0:
        return knowresults[change]
    else:
        for i in [c for c in coinvaluelist if c <= change]:
            numcoins = 1 + find_change_4(coinvaluelist, change - i, knowresults)
            if numcoins < mincoins:
                mincoins = numcoins
                knowresults[change] = mincoins
    return mincoins


# print(find_change_1([1, 5, 10, 25], 63))  # [1,5,10,25],63贪心就可以找到最优解
# print(find_change_2([1, 5, 10, 25], 63))
# print(find_change_1([1, 5, 10, 21, 25], 63))  # [1,5,10,25],63贪心就找不到最优解
# print(find_change_2([1, 5, 10, 21, 25], 63))
print(find_change_3([1, 5, 10, 21, 25], 63, [0] * 64))
