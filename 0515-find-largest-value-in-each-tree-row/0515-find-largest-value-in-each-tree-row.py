# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from typing import List, Optional

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # 初始化一個deque來存放當前層的節點
        queue = deque([root])
        # 用來存放每層的最大值
        res = []
        
        # 當還有節點在當前層時
        while queue:
            # 初始化當前層的最大值為負無窮大
            max_level = float('-inf')
            
            # 計算當前層的節點數量
            level_size = len(queue)
            # 對當前層的每一個節點進行操作
            for _ in range(level_size):
                node = queue.popleft()
                # 當節點為空時，繼續下一個迭代
                if not node:
                    continue
                
                # 更新當前層的最大值
                max_level = max(max_level, node.val)
                # 把當前節點的左、右子節點加入到隊列中
                queue.extend([node.left, node.right])
            
            # 如果當前層有有效的最大值（不是負無窮大），則加入到結果中
            if max_level != float('-inf'):
                res.append(max_level)
                
        return res
"""
解題思路
這個問題可以透過層序遍歷（BFS）的策略來解決。層序遍歷是一種從樹的根開始，先遍歷完一層，然後再進入下一層的遍歷方式。Python中的deque是一個雙端隊列，用於支持從兩端進行高效插入和刪除。

時間複雜度分析：
這個算法需要遍歷樹的每一個節點一次，所以時間複雜度為 O(n)，其中 n 為樹的節點數量。

空間複雜度分析：
最壞的情況下，會存儲樹的最後一層的所有節點，所以空間複雜度為 O(n/2)=O(n)。
"""