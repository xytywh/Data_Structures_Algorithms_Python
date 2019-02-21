import unittest


# 这个堆接收键-值对，我们假设键是int类型
class BinHeap:
    """实现最小堆，即任意节点左右子树的值均小于该节点的值"""

    def __init__(self):
        """创建一个新的空二叉堆对象,之所以要包含一个0，是为了让跟节点下标从1开始"""
        self.heapList = [0]
        self.currentSize = 0

    def insert(self, k):
        """
        假如一个新数据项到堆中
        :param k: FooThing对象 例如 ft = FoolThing(1,'a')
        :return:
        """
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percUp(self, i):
        while i // 2 > 0:
            # 将最小的节点移到根节点处
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
            i = i // 2

    def delMin(self):
        """返回堆中的最小项,同时从堆中删除"""
        if self.currentSize == 0:
            print('error!')
            return
        retval = self.heapList[1]
        # 先用最后一个节点代替根节点，再将新节点“下沉”来恢复堆次序
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, alist):
        """从一个 key 列表创建新堆"""
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        print(len(self.heapList), i)
        while (i > 0):
            print(self.heapList, i)
            self.percDown(i)
            i = i - 1
        print(self.heapList, i)

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc

    def minChild(self, i):
        """返回某个节点的两个子节点中较小的那个"""
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def isEmpty(self):
        """返回堆是否为空"""
        if currentSize == 0:
            return True
        else:
            return False

    def size(self):
        """返回堆中数据项的个数"""
        return self.currentSize


class FooThing:
    def __init__(self, x, y):
        self.key = x
        self.val = y

    def __lt__(self, other):
        """重载 < 运算符"""
        if self.key < other.key:
            return True
        else:
            return False

    def __gt__(self, other):
        """重载 > 运算符"""
        if self.key > other.key:
            return True
        else:
            return False

    def __hash__(self):
        """自定义对象调用 hash()"""
        return self.key


# class TestBinHeap(unittest.TestCase):
#     def setUp(self):
#         self.theHeap = BinHeap()
#         self.theHeap.insert(FooThing(5, 'a'))
#         self.theHeap.insert(FooThing(9, 'd'))
#         self.theHeap.insert(FooThing(1, 'x'))
#         self.theHeap.insert(FooThing(2, 'y'))
#         self.theHeap.insert(FooThing(3, 'z'))
#
#     def testInsert(self):
#         assert self.theHeap.currentSize == 5
#
#     def testDelmin(self):
#         assert self.theHeap.delMin().val == 'x'
#         assert self.theHeap.delMin().val == 'y'
#         assert self.theHeap.delMin().val == 'z'
#         assert self.theHeap.delMin().val == 'a'
#
#     def testMixed(self):
#         myHeap = BinHeap()
#         myHeap.insert(9)
#         myHeap.insert(1)
#         myHeap.insert(5)
#         assert myHeap.delMin() == 1
#         myHeap.insert(2)
#         myHeap.insert(7)
#         assert myHeap.delMin() == 2
#         assert myHeap.delMin() == 5
#
#     def testDupes(self):
#         myHeap = BinHeap()
#         myHeap.insert(9)
#         myHeap.insert(1)
#         myHeap.insert(8)
#         myHeap.insert(1)
#         assert myHeap.currentSize == 4
#         assert myHeap.delMin() == 1
#         assert myHeap.delMin() == 1
#         assert myHeap.delMin() == 8
#
#     def testBuildHeap(self):
#         myHeap = BinHeap()
#         myHeap.buildHeap([9, 5, 6, 2, 3])
#         f = myHeap.delMin()
#         print("f = ", f)
#         assert f == 2
#         assert myHeap.delMin() == 3
#         assert myHeap.delMin() == 5
#         assert myHeap.delMin() == 6
#         assert myHeap.delMin() == 9


if __name__ == '__main__':
    bh = BinHeap()
    bh.insert(FooThing(12, 'a'))
    print(bh, bh.size())
    bh.insert(FooThing(10, 'b'))
    print(bh, bh.size())

    # d = {}
    # d[FooThing(1, 'z')] = 10
    # unittest.main()
