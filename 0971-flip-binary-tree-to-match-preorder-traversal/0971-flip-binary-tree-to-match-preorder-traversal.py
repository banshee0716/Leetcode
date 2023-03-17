# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root, voyage):
        self.ans, self.ind = [], 0
        
        def dfs(node):
            if not node or self.ind == len(voyage): return
            if node.val != voyage[self.ind]: 
                self.ans.append(None)
                return
            dr, self.ind = 1, self.ind + 1
            
            if node.left and node.left.val != voyage[self.ind]:
                self.ans.append(node.val)
                dr = -1
                
            for child in [node.left, node.right][::dr]:
                dfs(child)
                
        dfs(root)
        return [-1] if None in self.ans else self.ans