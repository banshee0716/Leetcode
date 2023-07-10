# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # 如果節點為空，則返回0
        if not root:
            return 0
        
        # 遞迴地找出左子樹和右子樹的最小深度
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        
        # 如果節點的左子樹和右子樹都存在，則返回左子樹和右子樹的最小深度+1
        if root.left and root.right:
            return min(left, right) + 1
        
        # 否則，返回左子樹和右子樹的最大深度+1
        return max(left, right) + 1


"""
時間複雜度為 O(n)
其中 n 是樹的節點數量。這是因為我們需要遍歷每一個節點來計算其深度。

空間複雜度為 O(h)
其中 h 是樹的高度。這是因為在遞迴調用中，我們需要一個大小為 h 的調用棧，其中 h 是從根節點到最遠的葉子節點的路徑上的節點數量。
"""
        