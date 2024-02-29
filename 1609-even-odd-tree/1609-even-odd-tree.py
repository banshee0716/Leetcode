# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isEvenOddTree(self, root):
        if not root:
            return True

        queue = deque([root])
        level = 0

        while queue:
            prev_val = None
            for _ in range(len(queue)):
                node = queue.popleft()
                
                if ((level % 2 == 0 and (node.val % 2 == 0 or (prev_val is not None and node.val <= prev_val))) or
                   (level % 2 == 1 and (node.val % 2 == 1 or (prev_val is not None and node.val >= prev_val)))):
                    return False

                prev_val = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

        return True

    """
解題思路
廣度優先搜索（BFS）：
    -使用隊列進行層次遍歷（BFS），檢查每一層的節點是否符合奇偶樹的條件。

檢查條件：
    -在每一層開始遍歷之前，初始化一個變量prev_val來記錄該層前一個節點的值。
    -對於每個節點，根據其所在層是奇數層還是偶數層，檢查節點的值是否符合對應的奇偶性要求，並且與前一個節點的值比較是否符合遞增（偶數層）或遞減（奇數層）的要求。
    -如果有任何一個節點不符合要求，立即返回False。

遍歷子節點：
    -如果當前節點有左子節點或右子節點，將它們加入隊列以便後續處理。

返回結果：
    -如果所有層都符合奇偶樹的要求，則返回True。    

時間複雜度
    -遍歷樹的時間複雜度為O(N)，其中N是樹中節點的數量。

空間複雜度
    -需要額外的空間來存儲隊列，最壞情況下（完全二叉樹）空間複雜度為O(N)。然而，由於隊列中最多只存儲一層的節點，所以在實際應用中空間複雜度接近於O(寬度)，其中寬度是樹的最大層寬。
    """