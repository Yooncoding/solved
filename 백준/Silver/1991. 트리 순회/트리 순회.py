from sys import stdin

input = stdin.readline

n = int(input().rstrip())
tree = dict()
for _ in range(n):
    root, left, right = input().rsplit()
    tree[root] = [left, right]

def preorder_traversal(root):
    if root != '.':
        print(root, end='')
        preorder_traversal(tree[root][0])
        preorder_traversal(tree[root][1])


def inorder_traversal(root):
    if root != '.':
        inorder_traversal(tree[root][0])
        print(root, end='')
        inorder_traversal(tree[root][1])


def postorder_traversal(root):
    if root != '.':
        postorder_traversal(tree[root][0])
        postorder_traversal(tree[root][1])
        print(root, end='')


preorder_traversal('A')
print()
inorder_traversal('A')
print()
postorder_traversal('A')

