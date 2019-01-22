from pythonds.basic.queue import Queue


# 本书中实现的一个简单的python包，包含栈 队列 二叉树 图 等python实现


def hotpotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)
    # 现在的队列是["Brad", "Kent", "Jane", "Susan", "David", "Bill"]
    # 从Bill开始数，逆时针
    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()
    return simqueue.dequeue()


# 从Bill开始数，Bill是0，顺时针，数到7是下一个要出去的
print(hotpotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))
