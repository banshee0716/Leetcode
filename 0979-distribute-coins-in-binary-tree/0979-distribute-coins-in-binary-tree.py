# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.total_moves = 0  # 初始化類變數來紀錄總移動次數

        def dfs(node):
            if not node:
                return 0
            
            # 遞歸計算左右子節點的過剩或缺少硬幣數
            left_excess = dfs(node.left)
            right_excess = dfs(node.right)
            
            # 更新總移動次數，絕對值為當前節點的貢獻
            self.total_moves += abs(left_excess) + abs(right_excess)
            
            # 當前節點的硬幣過剩或缺少總數
            return node.val + left_excess + right_excess - 1
        
        dfs(root)
        return self.total_moves

# 使用 black 進行格式化


        
    """
題目描述
這道題目提供了一個二叉樹，每個節點上有一定數量的硬幣。目標是通過移動硬幣使得每個節點上只有一枚硬幣。需要返回實現這個目標的最小移動次數。

解題思路
這題可以用遞歸的方式來解決。主要的思想是使用後序遍歷，從底向上計算每個節點過剩或缺少的硬幣數量，並根據這個數量進行調整。

遞歸遍歷：對每個節點，先遍歷其左右子節點。
計算移動次數：對於每個節點，計算它與其子節點之間需要移動的硬幣數。這個數字是當前節點的值減去1（每個節點需要1個硬幣）。
更新父節點的硬幣數：將當前節點的硬幣數調整後的差值加到父節點上。
返回總移動次數：每次移動都是當前節點與其子節點之間的差的絕對值。

時間複雜度和空間複雜度
時間複雜度：O(N)，其中N是樹中的節點數，每個節點遍歷一次。
空間複雜度：O(H)，其中H是樹的高度，主要消耗在遞歸棧上。
    """