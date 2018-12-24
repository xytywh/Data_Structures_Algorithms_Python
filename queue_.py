class Queue():
    def __init__(self):
        self.__list = []

    # 入队和出队肯定有一个时间复杂度是O(1)，另一个是O(n)，具体选用哪种方式
    # 取决于实际操作的时候是入队操作更多还是出队操作更多
    def enqueue(self, item):
        """往队列中添加一个item元素"""
        self.__list.append(item)
        # self.__list.insert(0, item)

    def dequeue(self):
        """从队列头部删除一个元素"""
        return self.__list.pop(0)
        # return self.__list.pop()


    def is_empty(self):
        """判断一个队列是否为空"""
        return not self.__list

    def size(self):
        """返回队列的大小"""
        return len(self.__list)


# 在python中，以下对象是False,"" 0 [] {} 可以直接进行逻辑判断

if __name__ == "__main__":
    q = Queue()
    print(q.is_empty())
    print(q.size())
    q.enqueue(1)
    q.enqueue(2)
    print(q.size())
    print(q.dequeue())
    print(q.dequeue())
    print(q.size())
