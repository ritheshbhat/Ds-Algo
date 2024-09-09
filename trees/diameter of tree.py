from trees import tree_creation


def max_diameter(root):
    d = [0]
    h = [0]
    def postorder(root):
        if not root:
            return 0
        left = postorder(root.left)
        right = postorder(root.right)
        d[0] = max(d[0], (left + right))
        # h[0] = max(h[0], max(left,right)+1)
        return max(left, right) + 1

    postorder(root)
    print(d[0])
    # print('height is', h[0])


root =  [-10,9,20,None,None,15,7]
# root = [4, -7, -3, None, None, -9, -3, 9, -7, -4, None, 6, None, -6, -6, None, None, 0, 6, 5, None, 9, None, None, -1,
#         -4, None, None, None, -2]
root = tree_creation.create_tree(root)
max_diameter(root)
