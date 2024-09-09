

def postorder(root):
    if not root:
        return 0

    postorder(root.left)
    postorder(root.right)
    print(root.val)

from trees import tree_creation

root = [-10, 9, 20, None, None, 15, 7]
root = tree_creation.create_tree(root)
postorder(root)