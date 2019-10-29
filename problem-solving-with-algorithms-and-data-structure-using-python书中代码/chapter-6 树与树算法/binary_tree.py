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
        """利用队列实现二叉树的广度遍历(BFS，又叫层次遍历)"""
        if self.root is None:
            return None
        # 若不加上述判断的话，如果树为空，则queue=[None]
        # 那么bool(queue)为真，会往下执行，但是None没有lchild
        # 会出错
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end=" ")
            # 先往队列中插入左节点，再插右节点，这样出队就是先左节点后右节点了
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    # 树的三种深度遍历方式(DFS,使用递归)
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

    # 树的三种深度遍历方式(DFS，不使用非递归，利用栈)
    def preorder_stack(self):
        """利用栈实现二叉树的先序遍历"""
        if self.root is None:
            return
        cur_node = self.root
        stack = []
        while (stack or cur_node):
            while cur_node:
                # 先输出值之后，再入栈
                print(cur_node.elem, end=" ")
                stack.append(cur_node)
                cur_node = cur_node.lchild
            # if stack: 加不加不影响
            cur_node = stack.pop()
            cur_node = cur_node.rchild

            # 与上面一段是等价的
            # if cur_node:
            #     print(cur_node.elem, end=" ")
            #     stack.append(cur_node)
            #     cur_node = cur_node.lchild
            # else:
            #     cur_node = stack.pop()
            #     cur_node = cur_node.rchild

    def preorder_stack_1(self):
        """玩转算法面试 从真题到思维全面提升算法思维，利用栈实现二叉树的先序遍历，可以推广到中序和后序"""
        if self.root is None:
            return
        stack = []
        stack.append(['go', self.root])
        while stack:
            cur_node = stack.pop()
            if cur_node[0] == 'print':
                print(cur_node[1].elem, end=" ")
            else:
                assert cur_node[0] == 'go'
                if cur_node[1].rchild:
                    stack.append(['go', cur_node[1].rchild])
                if cur_node[1].lchild:
                    stack.append(['go', cur_node[1].lchild])
                stack.append(['print', cur_node[1]])

    def preorder_stack_2(self):
        if self.root is None:
            return None

        stack = [self.root]

        while stack:
            root = stack.pop()
            if root is not None:
                print(root.elem, end=" ")
                if root.rchild is not None:
                    stack.append(root.rchild)
                if root.lchild is not None:
                    stack.append(root.lchild)

    def preorder_stack(self):
        """邓俊辉-数据结构，利用栈实现二叉树的先序遍历，但不能推广到中序和后序"""
        stack = []
        if self.root:
            stack.append(self.root)
        while stack:
            cur_node = stack.pop()
            print(cur_node.elem, end=" ")
            # 孩子入栈顺序，先右后左
            if cur_node.rchild:
                stack.append(cur_node.rchild)
            if cur_node.lchild:
                stack.append(cur_node.lchild)

    def preorder_stack(self):
        """邓俊辉-数据结构，利用栈实现二叉树的先序遍历，可以推广到中序和后序"""
        if self.root is None:
            return
        cur_node = self.root
        stack = []
        while (stack or cur_node):
            while cur_node:
                # 先输出值之后，再入栈
                print(cur_node.elem, end=" ")
                stack.append(cur_node.rchild)
                cur_node = cur_node.lchild
            cur_node = stack.pop()

    def inorder_stack(self):
        """利用栈实现二叉树的中序遍历"""
        if self.root is None:
            return
        cur_node = self.root
        stack = []
        while (stack or cur_node):
            # print(not stack,not cur_node)
            while cur_node:
                stack.append(cur_node)
                cur_node = cur_node.lchild
            # if stack:加不加不影响
            # 先出栈再输出值
            cur_node = stack.pop()
            print(cur_node.elem, end=" ")
            cur_node = cur_node.rchild

            # 与上面一段是等价的
            # if cur_node:
            #     stack.append(cur_node)
            #     cur_node = cur_node.lchild
            # else:
            #     cur_node = stack.pop()
            #     print(cur_node.elem, end=" ")
            #     cur_node = cur_node.rchild

    def inorder_stack_1(self):
        """玩转算法面试 从真题到思维全面提升算法思维，利用栈实现二叉树的中序遍历，可以推广到先序和后序"""
        if self.root is None:
            return
        stack = []
        stack.append(['go', self.root])
        while stack:
            cur_node = stack.pop()
            if cur_node[0] == 'print':
                print(cur_node[1].elem, end=" ")
            else:
                assert cur_node[0] == 'go'
                if cur_node[1].rchild:
                    stack.append(['go', cur_node[1].rchild])
                stack.append(['print', cur_node[1]])
                if cur_node[1].lchild:
                    stack.append(['go', cur_node[1].lchild])

    def postorder_stack(self):
        """利用栈实现二叉树的后序遍历"""
        if self.root is None:
            return
        # cur_node当前访问结点，last_node上次访问结点
        cur_node = self.root
        last_node = None
        # 先把cur_node移动到左子树最下边
        stack = []
        while cur_node:
            stack.append(cur_node)
            cur_node = cur_node.lchild
        while stack:
            # 走到这里，cur_node都是空，并已经遍历到左子树底端(看成扩充二叉树，则空，亦是某棵树的左孩子)
            cur_node = stack.pop()
            # 某一个结点被作为一个根节点访问的前提是：无右子树或右子树已被访问过
            if cur_node.rchild is None or cur_node.rchild == last_node:
                print(cur_node.elem, end=" ")
                # 修改最近被访问的节点
                last_node = cur_node
                # cur_node = None
            # /这里的else语句可换成带条件的else if:
            # else if (cur_node.lchild == last_node) // 若左子树刚被访问过，则需先进入右子树(根节点需再次入栈)
            # 因为：上面的条件没通过就一定是下面的条件满足。仔细想想！
            else:
                # 因为不满足条件，所以当前的结点还不能输出，所以当前结点再次入栈
                stack.append(cur_node)
                # 进入右子树，且可肯定右子树一定不为空
                cur_node = cur_node.rchild
                while cur_node:
                    stack.append(cur_node)
                    cur_node = cur_node.lchild
            # print([x.elem for x in stack])

    def postorder_stack_1(self):
        """玩转算法面试 从真题到思维全面提升算法思维，利用栈实现二叉树的后序遍历，可以推广到先序和中序"""
        if self.root is None:
            return
        stack = []
        stack.append(['go', self.root])
        while stack:
            cur_node = stack.pop()
            if cur_node[0] == 'print':
                print(cur_node[1].elem, end=" ")
            else:
                assert cur_node[0] == 'go'
                stack.append(['print', cur_node[1]])
                if cur_node[1].rchild:
                    stack.append(['go', cur_node[1].rchild])
                if cur_node[1].lchild:
                    stack.append(['go', cur_node[1].lchild])

    def postorder_stack_2(self):
        if self.root is None:
            return []
        stack = [self.root]
        out = []
        while stack:
            item = stack.pop()
            if item:
                out.append(item.elem)
                if item.lchild:
                    stack.append(item.lchild)
                if item.rchild:
                    stack.append(item.rchild)
        # 后序遍历为 左右根, 只需要将上一步的输出 倒序
        print(' '.join([str(x) for x in out[::-1]]))


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
    bt.preorder_stack_2()
    print("")
    print("中序遍历(递归):", end=" ")
    bt.inorder_recursive(bt.root)
    print("")
    print("中序遍历(非递归):", end=" ")
    bt.inorder_stack_1()
    print("")
    print("后序遍历(递归):", end=" ")
    bt.postorder_recursive(bt.root)
    print("")
    print("后序遍历(非递归):", end=" ")
    bt.postorder_stack()
