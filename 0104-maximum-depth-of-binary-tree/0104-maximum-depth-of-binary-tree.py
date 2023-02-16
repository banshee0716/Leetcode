# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, Depth):
            if not root:
                return Depth
            return max(dfs(root.left, Depth+1),dfs(root.right, Depth+1))
        
        return dfs(root, 0)