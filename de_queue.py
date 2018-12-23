class DeQueue():
    def __init__(self):
        self.__list = []

    def add_front(self, item):
        """从队头加入一个item元素"""
        self.__list.insert(0, item)


    def add_rear(self, item):
        """从队尾加入一个item元素"""
        self.__list.append(item)

    def remove_front(self):
        """"从队头删除一个item元素"""
        return self.__list.pop(0)

    def remove_rear(self):
        """从队尾删除一个item元素"""
        return self.__list.pop()

    def is_empty(self):
        """判断双端队列是否为空"""
        return self.__list == []

    def size(self):
        """返回队列的大小"""
        return len(self.__list)


# 在python中，以下对象是False,"" 0 [] {} 可以直接进行逻辑判断


if __name__ == "__main__":
    dq = DeQueue()
    print(dq.is_empty())
    dq.add_front(2)
    dq.add_front(1)
    dq.add_rear(3)
    dq.add_rear(4)
    print(dq.remove_front())
    print(dq.remove_rear())
    print(dq.size())

