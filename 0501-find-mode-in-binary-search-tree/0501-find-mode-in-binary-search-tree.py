# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List
import collections

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        # 初始化一個列表來存儲中序遍歷的結果
        self.inorder_val = []
        
        # 定義一個中序遍歷的函數
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.inorder_val.append(root.val)
            inorder(root.right)
        
        # 對二元樹進行中序遍歷
        inorder(root)
        
        # 使用collections.Counter來計算每個元素出現的次數
        freq = collections.Counter(self.inorder_val)
        
        # 找到出現次數最多的元素的次數
        maxx = max(freq.values())
        
        # 遍歷計數器的keys，將出現次數等於最大次數的元素加入結果列表
        return [x for x in freq if freq[x] == maxx]

        
    
    """
給定具有重複項的二元搜尋樹 (BST) 的根，傳回其中的所有眾數（即最常出現的元素）。

如果樹有多個模式，則按任意順序傳回它們。

假設 BST 定義如下：

    -節點的左子樹僅包含鍵小於或等於該節點鍵的節點。
    -節點的右子樹僅包含鍵大於或等於該節點鍵的節點。
    -左子樹和右子樹也必須是二元搜尋樹。
    
    
解題思路：

1. 首先，我們需要對二元搜尋樹進行中序遍歷，因為中序遍歷可以得到一個從小到大排序的序列。
2. 然後，我們使用collections.Counter來計算每個元素出現的次數。
3. 接下來，我們找到出現次數最多的元素的次數。
4. 最後，我們遍歷計數器的keys，將出現次數等於最大次數的元素加入結果列表。


時間複雜度分析：
整體時間複雜度是O(N)。

空間複雜度分析：
整體空間複雜度是O(N)。
    """