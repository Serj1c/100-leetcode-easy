class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def closest_bst_value(root: TreeNode, target: float) -> int:
    
    def dfs(node, cur, target):
        if not node:
            return cur
        
        if cur == target:
            return cur
        
        if abs(node.val - target) < abs(cur - target):
            cur = node.val

        if target > node.val:
            kid = dfs(node.right, cur, target)
        else:
            kid = dfs(node.left, cur, target)

        return kid

    return dfs(root, float('inf', target))