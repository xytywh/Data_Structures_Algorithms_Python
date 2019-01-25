def BinaryTree(r):
    return [r, [], []]


def insertLeft(root, newBranch):
    """
    将结点newBranch插入到树root的根节点的左边
    :param root: 一棵树
    :param newBranch: 待插入结点
    :return: 插入节点后的新树
    """
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root


def insertRight(root, newBranch):
    """
    将结点newBranch插入到树root的根节点的右边
    :param root: 一棵树
    :param newBranch: 待插入结点
    :return: 插入节点后的新树
    """
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root


def getRootVal(root):
    return root[0]


def setRootVal(root, newVal):
    root[0] = newVal


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]


# 如果不加下面一句，那么在别的文件中导入此文件时，下面的结果也会显示出来
if __name__ == '__main__':
    r = BinaryTree(3)
    insertLeft(r, 4)
    insertLeft(r, 5)
    insertRight(r, 6)
    insertRight(r, 7)
    print(r)
    l = getLeftChild(r)
    print(l)

    setRootVal(l, 9)
    print(r)
    insertLeft(l, 11)
    print(r)
    print(getRightChild(getRightChild(r)))
