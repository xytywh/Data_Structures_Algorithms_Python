import random


# python基础教程(第三版 9.8)

def conflict(state, nextX):
    """
    如果是八皇后,那么state[i] = k 0<=i,k<=7
    :param state:list,state[i]代表第i+1行元素所在的列
    :param nextX: state中最后一个的元素的下一行所在的列
    :return:判断nextX是否与state中已有的列冲突(因为state中是按行存的，所以行的冲突不需要再考虑了，只考虑列和对角线)
    """
    # 下一个皇后所在的行
    nextY = len(state)
    for i in range(nextY):
        # 如果下一个皇后和当前皇后的水平距离为0（在同一列）或与它们的垂直距离相等（位于一
        # 条对角线上），这个表达式就为真；否则为假
        # 如果nextX已经在state（在同一列）中，或者nextX与state中某个元素的差值等于他们行的差值（在同一对角线）
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False


def queens_1(num, state):
    """
    如果只剩下最后一个皇后没有放好，就遍历所有可能的位置，并返回那
    些不会引发冲突的位置
    :param num: 皇后的个数，比如 4、8
    :param state:
    :return:
    """
    if len(state) == num - 1:
        for pos in range(num):
            if not conflict(state, pos):
                yield pos


def queens_2(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                # 只含有一个元素的元组必须要加, 否则就相当于一个数字
                yield (pos,)
            else:
                for result in queens_2(num, state + (pos,)):
                    yield (pos,) + result


def prettyprint(solution):
    def line(pos, length=len(solution)):
        return '. ' * (pos) + 'X ' + '. ' * (length - pos - 1)

    for pos in solution:
        print(line(pos))


if __name__ == '__main__':
    # 4个皇后(4*4棋盘) ,前三行分别放在第1 3 0 列，则第四行还有几个位置？显然只有2一个位置了
    print(list(queens_1(4, (1, 3, 0))))
    print(list(queens_2(3)))
    print(list(queens_2(4)))
    print(len(list(queens_2(8))), list(queens_2(8)))
    print(prettyprint(random.choice(list(queens_2(8)))))

# def queen(A, cur=0):
#     if cur == len(A):
#         print(A)
#         return 0
#     for col in range(len(A)):
#         A[cur], flag = col, True
#         for row in range(cur):
#             if A[row] == col or abs(col - A[row]) == cur - row:
#                 flag = False
#                 break
#         if flag:
#             queen(A, cur+1)
# queen([None]*8)
