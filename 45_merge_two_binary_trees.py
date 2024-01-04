class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def merge_trees(root1: TreeNode, root2: TreeNode) -> TreeNode:
    if not root1 and not root2:
        return None
    
    if not root1:
        return root2
    
    if not root2:
        return root1
    
    new_root = TreeNode(root1.val + root2.val)

    new_root.left = merge_trees(root1.left, root2.left)
    new_root.right = merge_trees(root1.right, root2.right)

    return new_root