class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item


# Preorder traversal
def preorder(root):
    if root:
        print(str(root.val) + "->", end="")
        preorder(root.left)
        preorder(root.right)


# Inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.val) + "->", end="")
        inorder(root.right)


# Postorder traversal
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.val) + "->", end="")
