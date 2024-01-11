class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def find_target(root: TreeNode, k: int) -> bool:
    seen = set()
    stack = [root]
    while stack:
        cur = stack.pop()
        if k - cur.val in seen:
            return True
        seen.add(cur.val)

        if cur.left:
            stack.append(cur.left)
        if cur.right:
            stack.append(cur.right)
    return False