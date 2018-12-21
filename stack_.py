class Stack():
    def __init__(self):
        self.__list = []

    def push(self, item):
        """添加一个新的元素item到栈顶"""
        self.__list.append(item)
        # 代表从尾部操作，时间复杂度为O(1)
        # 要是用链表实现的话从头操作更好

    def pop(self):
        """弹出栈顶元素"""
        if not self.__list:
            pass
            return
        return self.__list.pop()
        # 代表从尾部操作，时间复杂度为O(1)
        # 要是用链表实现的话从头操作更好

    def peek(self):
        """返回栈顶元素"""
        # 下面两句是等价的
        if self.__list:
            return self.__list.pop()
            # return self.__list[-1]
        else:
            return None

    def is_empty(self):
        """判断栈是否为空"""
        # 下面两种写法更推荐第二种
        # return len(self.__list) == 0
        # return self.__list == []
        return not self.__list

    def size(self):
        """ 返回栈的元素个数"""
        return len(self.__list)


# 在python中，以下对象是False,"" 0 [] {} 可以直接进行逻辑判断

if __name__ == "__main__":
    s = Stack()
    print(s.peek())
    print(s.is_empty())
    print(s.size())
    s.push(3)
    s.push(4)
    print(s.size())
    print(s.is_empty())
    s.pop()
    print(s.peek())
    s.pop()
    print(s.peek())
    s.pop()
