class Node():
    """节点"""

    def __init__(self, elem):
        self.elem = elem
        self.prev = None
        self.next = None


class DoubleLinkList():
    """双向链表"""

    def __init__(self, node=None):
        # __head 双下划线代表是私有变量
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def length(self):
        """链表长度"""
        # cur游标，用来移动遍历节点
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        """链表头部添加元素，头插法"""
        node = Node(item)
        node.next = self.__head

        # 下面两种不同顺序的执行情况是等价的

        self.__head = node
        node.next.prev = Node

        # self.__head.prev = node
        # self.__head = node

    def append(self, item):
        """链表尾部添加元素，尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        """指定位置添加元素
        :param pos 从0开始
        """
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            cur = self.__head
            count = 0
            while count < pos:
                count += 1
                cur = cur.next
            # 当循环退出时，cur指向pos位置
            node = Node(item)
            # 先不打断原有的链表顺序，先操作node本身
            node.next = cur
            node.prev = cur.prev

            # 下面两种不同顺序的执行情况是等价的

            cur.prev.next = node
            cur.prev = node

            # cur.prev = node
            # node.prev.next = node

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                # 先判断此结点是否是头结点
                if cur == self.__head:
                    if cur.next:
                        # 判断链表是否只有一个结点
                        cur.next.prev = cur.prev
                    self.__head = cur.next
                else:
                    cur.prev.next = cur.next
                    # 判断删除的是否是尾结点
                    if cur.next:
                        cur.next.prev = cur.prev
                # 删除元素之后，退出
                break
            else:
                cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            cur = cur.next
        return False


# 测试
if __name__ == "__main__":
    ll = DoubleLinkList(Node(80))
    print(ll.is_empty())
    print(ll.length())
    ll.append(1)
    ll.travel()
    print(ll.is_empty())
    print(ll.length())

    ll.add(8)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.insert(-1, 9)
    ll.travel()
    ll.insert(10, 7)
    ll.travel()
    ll.insert(2, 3)
    ll.travel()
    print(ll.search(10))
    ll.remove(9)
    ll.travel()
