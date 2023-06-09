#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(root, side):
            if not root:
                return 1
            return (
                dfs(root.left, side) + 1 if side == "l" else dfs(root.right, side) + 1
            )

        l = dfs(root.left, "l")
        r = dfs(root.right, "r")
        if l == r:
            return pow(2, l) - 1

        return self.countNodes(root.left) + self.countNodes(root.right) + 1


# @lc code=end
