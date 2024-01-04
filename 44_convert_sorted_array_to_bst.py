class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sorted_array_to_bst(nums):
    def helper(l, r):
        if l <= r:
            mid = (l + r) // 2
            node = TreeNode(nums[mid])

            node.left = helper(l, mid - 1)
            node.right = helper(r, mid + 1)
        return node
    return helper(0, len(nums)-1)