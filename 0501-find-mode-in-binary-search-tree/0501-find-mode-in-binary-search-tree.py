# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.inorder_val = []
        def inorder(root):
            if not root:
                return None
            self.inorder_val.append(root.val)
            inorder(root.left)
            inorder(root.right)
        
        inorder(root)
        freq = collections.Counter(self.inorder_val)
        maxx = max(freq.values())
        return [x for x in freq if freq[x] == maxx]
        
            
        
        
        
    
    """
給定具有重複項的二元搜尋樹 (BST) 的根，傳回其中的所有眾數（即最常出現的元素）。

如果樹有多個模式，則按任意順序傳回它們。

假設 BST 定義如下：

    -節點的左子樹僅包含鍵小於或等於該節點鍵的節點。
    -節點的右子樹僅包含鍵大於或等於該節點鍵的節點。
    -左子樹和右子樹也必須是二元搜尋樹。
    """