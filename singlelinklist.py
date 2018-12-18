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
        # _head 下划线代表是私有的
        self._head = node

    def is_empty(self):
        """链表是否为空"""
        pass

    def length(self):
        """链表长度"""
        pass

    def travel(self):
        """遍历整个链表"""
        pass

    def add(self, item):
        """链表头部添加元素"""
        pass

    def append(self, item):
        """链表尾部添加元素"""
        pass

    def insert(self, pos, item):
        """指定位置添加元素"""
        pass

    def remove(self, item):
        """删除节点"""
        pass

    def search(self, item):
        """查找节点是否存在"""
        pass
