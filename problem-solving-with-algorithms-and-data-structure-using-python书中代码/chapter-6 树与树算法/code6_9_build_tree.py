from code6_7 import BinaryTree, insertLeft, insertRight, getLeftChild, getRightChild


def build_tree():
    r = BinaryTree('a')
    insertLeft(r, 'b')
    insertRight(r, 'c')
    insertRight(getLeftChild(r), 'd')
    insertLeft(getRightChild(r), 'e')
    insertRight(getRightChild(r), 'f')
    return r


print(build_tree())
