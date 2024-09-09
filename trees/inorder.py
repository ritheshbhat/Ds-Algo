from trees import tree_creation


def inorder(root):
    if not root:
        return 0
    inorder(root.left)
    print(root.val)
    inorder(root.right)


root =  [-10,9,20,None,None,15,7]
root = tree_creation.create_tree(root)
inorder(root)