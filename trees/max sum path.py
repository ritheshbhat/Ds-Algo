from trees import tree_creation


def max_sum_path(root):
    max_sum = [float('-inf')]

    def postorder(root, max_sum):
        if not root:
            return 0
        left = postorder(root.left, max_sum)
        right = postorder(root.right, max_sum)
        node_val = root.val + left + right
        max_sum[0] = max(max_sum[0], node_val)

        if max(left, right) > 0 and root.val > 0:
            return root.val + max(left, right)
        if root.val <= 0 and max(left, right) <= 0:
            return 0
        if root.val > 0 and max(left, right) <= 0:
            return root.val
    postorder(root, max_sum)
    print(max_sum)



if __name__ == "__main__":
    root =  [-10,9,20,None,None,15,7]
    root = tree_creation.create_tree(root)

    max_sum_path(root)

