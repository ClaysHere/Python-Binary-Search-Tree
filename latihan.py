class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(node,key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(str(root.key), end=' ')
        inorder(root.right)

def preorder(root):
    if root is not None:
        print(str(root.key), end=' ')
        preorder(root.left)
        preorder(root.right)
        
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(str(root.key), end=' ')
    
root = None

n = int(input('Jumlah data = '))

for i in range(n):
    temp = int(input(f'Masukkan data ke-{i+1} = '))
    root = insert(root, temp)

print()

print('Inorder traversal:', end=' ')
inorder(root)
print()

print('preorder traversal:', end=' ')
preorder(root)
print()

print('postorder traversal:', end=' ')
postorder(root)
print()
