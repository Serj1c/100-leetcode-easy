class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val


def post_order_traversal(root: TreeNode):
    ans = []

    def helper(node):
        if node:
            helper(node.left)
            helper(node.right)
            ans.append(node.val)

    helper(root)
    return ans
