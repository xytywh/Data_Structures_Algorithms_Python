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
    def preorder_recursive(self, node):
        """递归实现先序遍历"""
        if node is None:
            return
        print(node.elem, end=" ")
        self.preorder_recursive(node.lchild)
        self.preorder_recursive(node.rchild)

    def inorder_recursive(self, node):
        """递归实现中序遍历"""
        if node is None:
            return
        self.inorder_recursive(node.lchild)
        print(node.elem, end=" ")
        self.inorder_recursive(node.rchild)

    def postorder_recursive(self, node):
        """递归实现后序遍历"""
        if node is None:
            return
        self.postorder_recursive(node.lchild)
        self.postorder_recursive(node.rchild)
        print(node.elem, end=" ")

    # 树的三种深度遍历方式(非递归，利用栈)
    def preorder_stack(self):
        """利用栈实现二叉树的先序遍历"""
        if self.root is None:
            return
        cur_node = self.root
        stack = []
        while (stack or cur_node):
            while cur_node:
                print(cur_node.elem, end=" ")
                stack.append(cur_node)
                cur_node = cur_node.lchild
            if stack:
                cur_node = stack.pop()
                cur_node = cur_node.rchild

    def inorder_stack(self):
        """利用栈实现二叉树的中序遍历"""
        if self.root is None:
            return
        cur_node = self.root
        stack = []
        while (stack or cur_node):
            while cur_node:
                stack.append(cur_node)
                cur_node = cur_node.lchild
            if stack:
                cur_node = stack.pop()
                print(cur_node.elem, end=" ")
                cur_node = cur_node.rchild

    def postorder_stack(self):
        """利用栈实现二叉树的后序遍历"""
        if self.root is None:
            return
        # cur_node当前访问结点，last_node上次访问结点
        cur_node = self.root
        last_node = None
        stack = []
        while cur_node:
            stack.append(cur_node)
            cur_node = cur_node.lchild
        while stack:
            cur_node = stack.pop()
            if cur_node.rchild is None or cur_node.rchild == last_node:
                print(cur_node.elem, end=" ")
                last_node = cur_node
            else:
                stack.append(cur_node)
                cur_node = cur_node.rchild
                while cur_node:
                    stack.append(cur_node)
                    cur_node = cur_node.lchild


if __name__ == "__main__":
    bt = BinaryTree()
    for i in range(0, 10):
        bt.add(i)
    print("层次遍历:", end=" ")
    bt.breadth_travel()
    print("")
    print("先序遍历(递归):", end=" ")
    bt.preorder_recursive(bt.root)
    print("")
    print("先序遍历(非递归):", end=" ")
    bt.preorder_stack()
    print("")
    print("中序遍历(递归):", end=" ")
    bt.inorder_recursive(bt.root)
    print("")
    print("中序遍历(非递归):", end=" ")
    bt.inorder_stack()
    print("")
    print("后序遍历(递归):", end=" ")
    bt.postorder_recursive(bt.root)
    print("")
    print("后序遍历(非递归):", end=" ")
    bt.postorder_stack()
