from trees import tree_creation


def height_of_binary_tree(root):
    h = [0]
    def postorder(root):
        if not root:
            return 0

        left = postorder(root.left)
        right = postorder(root.right)
        h[0] = max(h[0], max(left, right)+1)
        return max(left,right) + 1
    postorder(root)
    print(h[0])


root =  [-10,9,20,None,None,15,7]
root = tree_creation.create_tree(root)
height_of_binary_tree(root)
