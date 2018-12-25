class Node():
    def __init__(self, item):
        self.elem = item
        self.lchild = None
        self.rchild = None


class BinaryTree():
    """"""

    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        # 若不加上述判断的话，如果树为空，则queue=[None]
        # 那么bool(queue)为真，会往下执行，但是None没有lchild
        # 会出错
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):
        """利用队列实现二叉树的广度遍历(层次遍历)"""
        if self.root is None:
            return None
        # 若不加上述判断的话，如果树为空，则queue=[None]
        # 那么bool(queue)为真，会往下执行，但是None没有lchild
        # 会出错
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end=" ")
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    # 树的三种深度遍历方式(递归)
    def preorder(self, node):
        """递归实现先序遍历"""
        if node is None:
            return
        print(node.elem, end=" ")
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def inorder(self, node):
        """递归实现中序遍历"""
        if node is None:
            return
        self.inorder(node.lchild)
        print(node.elem, end=" ")
        self.inorder(node.rchild)

    def postorder(self, node):
        """递归实现后序遍历"""
        if node is None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.elem, end=" ")


if __name__ == "__main__":
    bt = BinaryTree()
    bt.add(0)
    bt.add(1)
    bt.add(2)
    bt.add(3)
    bt.add(4)
    bt.add(5)
    bt.add(6)
    bt.add(7)
    bt.add(8)
    bt.add(9)
    print("层次遍历:", end=" ")
    bt.breadth_travel()
    print("")
    print("先序遍历:", end=" ")
    bt.preorder(bt.root)
    print("")
    print("中序遍历:", end=" ")
    bt.inorder(bt.root)
    print("")
    print("后序遍历:", end=" ")
    bt.postorder(bt.root)
