# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root):
        if root is None:
            return False  # 如果節點為None，適當處理（視情況而定，本題中不存在此情況）
        
        if root.val == 0:
            return False  # 0代表False
        elif root.val == 1:
            return True   # 1代表True
        elif root.val == 2:
            # 進行OR運算
            return self.helper(root.left) or self.helper(root.right)
        elif root.val == 3:
            # 進行AND運算
            return self.helper(root.left) and self.helper(root.right)

    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root)

        
        
    """
題目描述
給定一個由節點組成的二元樹，其中節點值為0（代表False）、1（代表True）、2（代表邏輯OR）、或3（代表邏輯AND）。樹的葉節點只包含0或1。需要根據給定的樹結構來評估這棵樹最終代表的布林值。

解題思路
遞歸方法：使用遞歸方式來解析每個節點的邏輯運算，基於節點的值來決定是執行AND、OR運算，或者直接返回節點的布林值。
基礎條件：如果節點值為0或1，則直接返回相應的布林值。
遞歸邏輯：對於邏輯運算節點（2: OR, 3: AND），遞歸調用左右子節點，根據遞歸結果執行對應的布林運算。


時間複雜度和空間複雜度
時間複雜度：O(N)，其中N是樹中的節點數量，每個節點都需要訪問一次。
空間複雜度：O(H)，其中H是樹的高度，主要消耗在遞歸棧上。
    """