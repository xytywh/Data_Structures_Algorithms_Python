# a = 10 #a中保存的是10所在的地址
# b = 20 #python中变量保存的是地址，变量是隐式的，所以可以指向任意对象
# a,b=b,a #把等号看作是改变指向，不要看做赋值


class Node():
    """节点"""

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleCycleLinkList():
    """单链表"""

    def __init__(self, node=None):
        # __head 双下划线代表是私有变量
        self.__head = node
        if node:
            node.next = node  # 或者node.next = self.__head

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def length(self):
        """链表长度"""
        if self.is_empty():
            return 0
        # cur游标，用来移动遍历节点
        cur = self.__head
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem, end=" ")
            cur = cur.next
        # 退出循环，cur指向尾结点，但尾结点的元素未打印
        print(cur.elem)

    def add(self, item):
        """链表头部添加元素，头插法"""
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            node = Node(item)
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # 退出循环，cur指向尾结点
            node.next = self.__head
            self.__head = node
            cur.next = node  # 或者cur.next = self.__head

    def append(self, item):
        """链表尾部添加元素，尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next

            # 下面两种写法等价

            node.next = cur.next  # 或者node.next = self.__head
            cur.next = node

            # cur.next = node
            # node.next = self.__head

    def insert(self, pos, item):
        """指定位置添加元素
        :param pos 从0开始
        """
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.next
            # 当循环退出时，pre指向pos-1位置
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除节点"""
        if self.is_empty():
            return
        pre = None
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                # 先判断此结点是否是头结点
                if cur == self.__head:
                    # 头结点的情况，找尾结点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    # 中间结点
                    pre.next = cur.next
                # 删除元素之后，退出
                # 这里一定要用return，退出整个函数体，用break会出错
                return
            else:
                pre = cur
                cur = cur.next
        # 退出循环，cur指向尾结点
        if cur.elem == item:
            if cur == self.__head:
                # 链表只有一个结点
                self.__head = None
            else:
                pre.next = cur.next

    def search(self, item):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            cur = cur.next
        if cur.elem == item:
            return True
        return False


# 测试
if __name__ == "__main__":
    # node = Node(80)
    # cur = node
    # for i in range(10):
    #     node.next = Node(i)
    #     node = node.next
    # while cur != None:
    #     print(cur.elem)
    #     cur = cur.next
    scll = SingleCycleLinkList(Node(80))
    print(scll.is_empty())
    print(scll.length())
    scll.append(1)
    scll.travel()
    print(scll.is_empty())
    print(scll.length())

    scll.add(8)
    scll.append(2)
    scll.append(3)
    scll.append(4)
    scll.append(5)
    scll.append(6)
    scll.insert(-1, 9)
    scll.travel()
    scll.insert(10, 7)
    scll.travel()
    scll.insert(2, 3)
    scll.travel()
    print(scll.search(10))
    scll.remove(9)
    scll.travel()
