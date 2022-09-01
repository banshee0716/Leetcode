# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root, max_value = -10000):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        return self.goodNodes(root.left, max(max_value, root.val)) + self.goodNodes(root.right, max(max_value, root.val)) + (root.val >= max_value) if root else 0