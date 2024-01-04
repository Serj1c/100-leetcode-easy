class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def binary_tree_paths(root: TreeNode):
    ans = []

    def dfs(node: TreeNode, path:str):
          if not node.right and not node.left:
               path += str(node.val) + '->'
               ans.append(path[:-2])
               return

          if node.left:
            dfs(node.left, path)
          if node.right:
            dfs(node.right, path)
    
    dfs(root, '')

    return ans