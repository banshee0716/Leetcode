# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.val = 0
        
        def dfs(node):
            if not node:
                return 
            dfs(node.right)
            self.val += node.val
            node.val = self.val
            dfs(node.left)
            
        dfs(root)
        return root
        
    
    """
給定二元搜尋樹 (BST) 的根，將其轉換為更大樹，使得原始 BST 的每個鍵都更改為原始鍵加上 BST 中大於原始鍵的所有鍵的總和。

提醒一下，二元搜尋樹是滿足以下限制的樹：

節點的左子樹僅包含鍵小於該節點鍵的節點。
節點的右子樹僅包含鍵大於該節點鍵的節點。
左子樹和右子樹也必須是二元搜尋樹。
    """