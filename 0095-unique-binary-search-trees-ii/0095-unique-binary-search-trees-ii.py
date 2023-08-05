# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:  # 若 n為0則返回空列表
            return []

        memo = {}  # 用於儲存已計算過的子問題的結果

        def generate_trees(start, end):
            if (start, end) in memo:  # 如果已經計算過，直接返回結果
                return memo[(start, end)]

            trees = []
            if start > end:  # 終止條件，若start大於end，則返回None
                trees.append(None)
                return trees

            for root_val in range(start, end + 1):  # 遍歷每個可能的根節點值
                left_trees = generate_trees(start, root_val - 1)  # 生成左子樹
                right_trees = generate_trees(root_val + 1, end)  # 生成右子樹

                for left_tree in left_trees:
                    for right_tree in right_trees:
                        root = TreeNode(root_val, left_tree, right_tree)  # 創建新的樹
                        trees.append(root)

            memo[(start, end)] = trees
            return trees

        return generate_trees(1, n)  # 從1到n生成樹

            
"""
給定一個整數 n，返回所有結構上唯一的 BST（二叉搜索樹），該樹恰好具有從 1 到 n 的唯一值的 n 個節點。以任意順序返回答案。


1. 我們使用遞迴的方法，每次選擇一個節點作為根節點，並生成左子樹和右子樹。
2. 左子樹包括比根節點小的所有值，右子樹包括比根節點大的所有值。
3. 我們遍歷所有可能的根節點值，並對每個可能的左、右子樹組合生成一個新的樹。
4. 為了避免重複計算，使用 memoization 儲存已經計算過的結果。

時間複雜度：
O(4^n / sqrt(n))，這個問題的時間複雜度非常難以直接分析，它與卡塔蘭數有關。
空間複雜度：
O(4^n / sqrt(n))，保存所有可能的二叉樹。
"""