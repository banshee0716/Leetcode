# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, 0, 0
            
            ls, lc, rl = dfs(node.left)
            rs, rc, rr = dfs(node.right)
            
            res = 0
            if (ls + rs + node.val) // (lc + rc +1) == node.val:
                res += 1
            return ls + rs + node.val, lc + rc + 1, res + rl + rr
       
        return dfs(root)[2]