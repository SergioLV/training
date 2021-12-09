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
            self._printTree(curr_node.left)
            self._printTree(curr_node.right)
            print(curr_node.data)

    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, curr_node, tree_height):
        if curr_node is None:
            return tree_height
        left_tree = self._height(curr_node.right, tree_height + 1)
        right_tree = self._height(curr_node.left, tree_height + 1)

        return max(left_tree, right_tree)


tree = BST()
tree.insert(25)
tree.insert(20)
tree.insert(36)
tree.insert(10)
tree.insert(22)
tree.insert(30)
tree.insert(40)
tree.insert(5)
tree.insert(12)
tree.insert(28)
tree.insert(38)
tree.insert(48)

# tree.printTree()
print(tree.height())
