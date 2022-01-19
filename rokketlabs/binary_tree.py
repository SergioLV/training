class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BST:
    def __init__(self):
        self.root = None


def printBst(root):
    if root:
        return _printBst(root)
    else:
        return "The tree is empty"


def _printBst(current):
    if current != None:
        print(current.value)
        _printBst(current.left)
        _printBst(current.right)


def invertBinaryTree(tree):
    if tree:
        left = tree.left
        right = tree.right
        right, left = invertBinaryTree(tree.left), invertBinaryTree(tree.right)
    return tree


if __name__ == '__main__':
    tree = BST()
    tree.root = Node(10)
    tree.root.left = Node(5)
    tree.root.right = Node(15)

    printBst(tree.root)
    inverted = invertBinaryTree(tree.root)
    printBst(inverted)
