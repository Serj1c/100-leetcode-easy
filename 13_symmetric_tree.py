from collections import deque


class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val


def is_symmetric(root: TreeNode):
    q = deque([root])
    while q:

        level = []
        for _ in range(len(q)):
            cur = q.popleft()
            level.append(cur.val if cur else None)

            if cur:
                q.append(cur.left)
                q.append(cur.right)

        if len(level) > 1:
            n = len(level)
            fh, sh = level[:n//2], level[n//2:][::-1]
            if fh != sh:
                return False

    return True
