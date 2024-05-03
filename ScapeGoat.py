import math

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ScapegoatTree:
    def __init__(self, alpha=0.75):
        self.root = None
        self.alpha = alpha
        self.size = 0

    def _size(self, node):
        return 0 if node is None else 1 + self._size(node.left) + self._size(node.right)

    def _insert(self, node, value):
        if node is None:
            return TreeNode(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)
        return node

    def insert(self, value):
        self.root = self._insert(self.root, value)
        self.size += 1
        if self._size(self.root) > 1 / self.alpha * math.log2(self.size):
            self._rebuild(self.root)

    def _rebuild(self, node):
        nodes = self._flatten(node)
        self.root = self._build(nodes, 0, len(nodes))

    def _flatten(self, node):
        nodes = []
        stack = []
        current = node
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                nodes.append(current)
                current = current.right
        return nodes

    def _build(self, nodes, start, end):
        if start >= end:
            return None
        mid = (start + end) // 2
        node = nodes[mid]
        node.left = self._build(nodes, start, mid)
        node.right = self._build(nodes, mid + 1, end)
        return node

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=" ")
            self.inorder_traversal(node.right)


# Example usage:
values = [10, 5, 15, 3, 7, 12, 17, 1, 4, 6, 8, 11, 14, 16, 18]

s_tree = ScapegoatTree()

for value in values:
    s_tree.insert(value)

print("Inorder traversal of Scapegoat tree:")
s_tree.inorder_traversal(s_tree.root)
