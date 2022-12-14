# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @cache
    def rob(self, root, canRob = True):
        if not root: return 0
        dont_rob = self.rob(root.left, True) + self.rob(root.right, True)
        rob_root = root.val + self.rob(root.left, False) + self.rob(root.right, False) if canRob else -1
        return max(dont_rob, rob_root)