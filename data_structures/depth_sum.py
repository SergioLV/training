def nodeDepths(root, depth=0):
    if root != None:
        a = root.data
        return nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth+1)
    return 0

# This is the class of the input binary tree.


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root != None:
            return self._insert(self.root, value)
        else:
            self.root = Node(value)

    def _insert(self, curr_node, value):
        if value < curr_node.data:
            if curr_node.left is None:
                curr_node.left = Node(value)
            else:
                return self._insert(curr_node.left, value)
        elif value > curr_node.data:
            if curr_node.right is None:
                curr_node.right = Node(value)
            else:
                return self._insert(curr_node.right, value)

    def printTree(self):
        if self.root != None:
            return self._printTree(self.root)
        else:
            return "The tree is empty!"

    def _printTree(self, curr_node):
        if curr_node != None:
            print(curr_node.data)
            self._printTree(curr_node.left)
            self._printTree(curr_node.right)


tree = BST()
tree.insert(10)
tree.insert(5)
tree.insert(1)
tree.insert(6)
tree.insert(19)
tree.insert(17)
tree.insert(21)
# tree.insert(Node(15))
# tree.printTree()
# print(tree.root.data)
print(nodeDepths(tree.root))
