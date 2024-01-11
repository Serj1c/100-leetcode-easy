class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def range_sum_of_bst(root: TreeNode, low: int, high: int) -> TreeNode:
    if not root:
        return 0
    left, right = 0, 0

    if root.val < high:
        right = range_sum_of_bst(root.right, low, high)
    if root.val > low:
        left = range_sum_of_bst(root.left, low, high)

    cur = root.val if low <= root.val <= high else 0

    return left + right + cur