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

def minValueNode(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current

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

def delete(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)
    return root

def fiTraversal(root):
    print('\nTraversal BST')
    print('='*30)
    print('1. Inorder traversal')
    print('2. Preorder traversal')
    print('3. Post order traversal')
    print('4. Keluar')
    pil = int(input('Masukkan pilihan menu (1 s.d. 4) = '))
    print()
    if pil == 1:
        print('Inorder traversal adalah:',end=' ')
        inorder(root)
        print()
        fitur(root,list)
    elif pil == 2:
        print('Preorder traversal adalah:',end=' ')
        preorder(root)
        print()
        fitur(root,list)
    elif pil == 3:
        print('Post order traversal adalah:',end=' ')
        postorder(root)
        print()
        fitur(root,list)
    elif pil == 4:
        fitur(root,list)
    else:
        print('Pilihan yang anda masukkan tidak tersedia')
        fiTraversal(root)

def fiturDelete(root,list):
    hapus = int(input('Masukkan data yang akan dihapus = '))
    if hapus in list:
        delete(root,hapus)
        print('Data sekarang:',end=' ')
        inorder(root)
        print()
    else:
        print('Data tidak ada di dalam tree')
        fiturDelete(root,list)

def fitur(root,list):
    print('\nPilihan Fitur')
    print('='*30)
    print('1. Masukkan data baru')
    print('2. Hapus data')
    print('3. Traversal')
    print('4. Keluar')
    pil = int(input('Masukkan pilihan menu (1 s.d. 4) = '))
    print()
    if pil == 1:
        new = int(input('Masukkan data baru = '))
        print(f'Data {new} telah ditambahkan')
        insert(root, new)
        print('Data sekarang:', end=' ')
        inorder(root)
        print()
        list.append(new)
        fitur(root,list)
    elif pil == 2:
        fiturDelete(root,list)
        fitur(root,list)
    elif pil == 3:
        fiTraversal(root)
    elif pil == 4:
        print('Terima kasih telah menggunakan program ini')


root = None
listData = []

n = int(input('Jumlah data = '))

for i in range(n):
    temp = int(input(f'Masukkan data ke-{i+1} = '))
    root = insert(root, temp)
    listData.append(temp)

print('Inorder traversal:',end=' ')
inorder(root)
print()

fitur(root,listData)
