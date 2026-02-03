class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def insert(root, val):
    if root is None:
        return Node(val)

    if val < root.data:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)

    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)



a = [3, 8, 1, 4, 2, 12, 6, 7]
root = None

for el in a:
    root = insert(root, el)
print(root)

print("Inorder traversal:")
inorder(root)

    

 
