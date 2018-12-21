# a = 10 #a中保存的是10所在的地址
# b = 20 #python中变量保存的是地址，变量是隐式的，所以可以指向任意对象
# a,b=b,a #把等号看作是改变指向，不要看做赋值


class Node():
    """节点"""

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList():
    """单链表"""

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
        self.__head = node

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
        pre = None
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                # 先判断此结点是否是头结点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                # 删除元素之后，退出
                break
            else:
                pre = cur
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
    # node = Node(80)
    # cur = node
    # for i in range(10):
    #     node.next = Node(i)
    #     node = node.next
    # while cur != None:
    #     print(cur.elem)
    #     cur = cur.next
    sll = SingleLinkList(Node(80))
    print(sll.is_empty())
    print(sll.length())
    sll.append(1)
    sll.travel()
    print(sll.is_empty())
    print(sll.length())

    sll.add(8)
    sll.append(2)
    sll.append(3)
    sll.append(4)
    sll.append(5)
    sll.append(6)
    sll.insert(-1, 9)
    sll.travel()
    sll.insert(10, 7)
    sll.travel()
    sll.insert(2, 3)
    sll.travel()
    print(sll.search(10))
    sll.remove(9)
    sll.travel()
