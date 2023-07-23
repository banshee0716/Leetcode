# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # 節點數為偶數的情況下不能形成滿二叉樹
        if n % 2 == 0:
            return []
        
        # 初始化記憶體 memo，用於儲存已經計算過的子問題結果
        memo = {}

        def _allPossibleFBT(n):
            # 如果已經計算過，直接從 memo 中取結果
            if n in memo:
                return memo[n]
            
            list = []
            if n == 1:
                # n為1時，創建一個節點並加入列表
                list.append(TreeNode(0))
            else:
                # n大於1時，將其分解為左子樹和右子樹，i為左子樹的節點數
                for i in range(1, n - 1, 2):
                    # 獲取所有可能的左、右子樹
                    lTrees = _allPossibleFBT(i)
                    rTrees = _allPossibleFBT(n - i - 1)

                    # 將所有可能的左、右子樹組合起來，形成新的樹
                    for lt in lTrees:
                        for rt in rTrees:
                            list.append(TreeNode(0, lt, rt))

            # 將結果儲存到 memo 中，以供後續使用
            memo[n] = list
            return list

        return _allPossibleFBT(n)

        
        
"""
1. 由於滿二叉樹的每個節點都有兩個子節點，因此其節點數必定為奇數。因此，解決方案首先檢查 n 是否為偶數，如果是，則返回空列表。

2. 接下來，定義了一個 memo 來儲存已經計算過的值，避免重複運算，這是動態規劃的一部分。

3. 接著定義一個內部函數 _allPossibleFBT，該函數會計算 n 節點的所有可能樹結構。在這個遞歸函數中，我們遍歷從 1 到 n-1 的所有奇數，分別計算左子樹和右子樹的所有可能結構，然後組合在一起，形成當前節點數 n 的所有可能樹結構。

4. 最後，將計算出的結果儲存到 memo 中，並返回該列表。

時間複雜度方面，由於我們用了動態規劃來避免重複計算，所以時間複雜度可以降低到 O(4^n / n^(3/2))（這是卡特蘭數的一種近似），其中 n 是樹的節點數。

在空間複雜度方面，我們儲存了子問題的結果，因此空間複雜度為 O(n)，其中 n 是樹的節點數。
"""