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

    def depth_travel(self, node=self.root):
        """二叉树的深度遍历"""
        pass


if __name__ == "__main__":
    bt = BinaryTree()
    bt.add('A')
    bt.add('B')
    bt.add('G')
    bt.add('C')
    bt.add('F')
    bt.add('H')
    bt.add('I')
    bt.add('D')
    bt.add('E')
    bt.add('J')
    bt.breadth_travel()
