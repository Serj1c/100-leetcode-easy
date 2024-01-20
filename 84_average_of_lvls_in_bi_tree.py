from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def averageOfLevels(root: TreeNode):
    ans = []
    q = deque([root])

    while q:
        summ = 0
        cnt = 0
        for _ in range(len(q)):
            cur = q.popleft()
            summ += cur.val
            cnt += 1

            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        ans.append(summ / cnt)
    return ans