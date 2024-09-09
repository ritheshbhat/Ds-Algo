from trees import tree_creation

def preorder(root):
    if not root:
        return 0
    print(root.val)
    preorder(root.left)
    preorder(root.right)


root =  [-10,9,20,None,None,15,7]
root = tree_creation.create_tree(root)
preorder(root)