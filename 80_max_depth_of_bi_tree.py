class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth_of_binary_tree(root: TreeNode) -> int:
    if root == None:
        return 0
    left = max_depth_of_binary_tree(root.left)
    right = max_depth_of_binary_tree(root.right)
    return max(left, right) * 1