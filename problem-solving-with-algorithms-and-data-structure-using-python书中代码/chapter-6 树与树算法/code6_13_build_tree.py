from code6_10 import BinaryTree


def build_tree():
    r = BinaryTree('a')
    r.insertLeft('b')
    r.insertRight('c')
    r.getLeftChild().insertRight('d')
    r.getRightChild().insertLeft('e')
    r.getRightChild().insertRight('f')
    return r


print(build_tree())
