class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert_level_order(arr, root, i, n):
    if i < n:
        if arr[i] is not None:
            temp = TreeNode(arr[i])
            root = temp

            # Insert left child
            root.left = insert_level_order(arr, root.left, 2 * i + 1, n)

            # Insert right child
            root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
        return root
    return None

def create_tree(arr):
    n = len(arr)
    return insert_level_order(arr, None, 0, n)
