# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(curr, num):
            if curr is None:
                return 0
                
            num = num * 10 + curr.val  # 更新當前路徑形成的數字
            if not curr.left and not curr.right:  # 判斷是否為葉子節點
                return num
            # 向左右子樹進行遞迴，並將結果相加
            return dfs(curr.left, num) + dfs(curr.right, num)
        
        return dfs(root, 0)  # 從根節點開始遞迴

    """
    
解題思路
這個問題可以透過深度優先搜索（DFS）來解決。對於每一個節點，你可以帶著目前形成的數字進行遞迴。當到達葉子節點時，返回當前形成的數字。如果不是葉子節點，則繼續向左右子樹進行遞迴，並將結果相加。

時間複雜度分析
遍歷每個節點一次以計算數字，所以時間複雜度為O(N)，其中N是二叉樹中節點的數量。

空間複雜度分析
在最壞情況下，即樹退化為鏈表時，遞迴調用將使用O(N)的空間。在平衡樹中，空間複雜度會是O(log N)。這取決於樹的高度。
    """