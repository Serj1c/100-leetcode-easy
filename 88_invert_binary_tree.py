class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def invert_tree(root: TreeNode) -> TreeNode:
    if not root:
        return None
    
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)

    return root