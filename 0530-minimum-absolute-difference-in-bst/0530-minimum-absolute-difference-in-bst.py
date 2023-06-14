# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min_diff = float('inf')  # 初始化最小差為無窮大
        self.prev = None  # 初始化上一個節點為 None

        def inorder(root):
            if not root:  # 若節點不存在，則返回
                return
            inorder(root.left)  # 遍歷左子樹
            if self.prev is not None:  # 若上一個節點存在，則計算當前節點與上一個節點的差，並更新最小差
                self.min_diff = min(self.min_diff, root.val - self.prev)
            self.prev = root.val  # 更新上一個節點為當前節點
            inorder(root.right)  # 遍歷右子樹

        inorder(root)  # 從根節點開始中序遍歷
        return self.min_diff  # 返回最小絕對差
"""
解題思路：

初始設定最小差為無窮大，上一個節點為 None。
定義一個中序遍歷的函數，若節點不存在，則返回；否則，先遍歷左子樹，然後計算當前節點與上一個節點的差，並更新最小差，接著更新上一個節點為當前節點，最後遍歷右子樹。
從根節點開始執行中序遍歷。
返回最小絕對差。

時間複雜度：
O(n)，其中 n 為二叉搜索樹的節點數量。因為我們需要遍歷整棵樹。

空間複雜度：
O(h)，其中 h 為二叉搜索樹的高度。在最壞情況下（樹呈線性結構），我們需要的額外空間由樹的高度決定，因為需要考慮遞迴棧的深度。

"""