# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:  # 特殊情況，新增一個根節點
            return TreeNode(val, root, None)
        
        def dfs(node, current_depth):
            if not node:
                return
            if current_depth == depth - 1:  # 到達插入行的上一行
                node.left = TreeNode(val, node.left, None)  # 插入新的左子節點
                node.right = TreeNode(val, None, node.right)  # 插入新的右子節點
            else:
                dfs(node.left, current_depth + 1)
                dfs(node.right, current_depth + 1)
                
        dfs(root, 1)  # 從根節點開始遞迴
        return root

    """
時間複雜度分析
遍歷到指定深度的所有節點，最壞情況下時間複雜度為O(N)，其中N是樹中的節點數量。

空間複雜度分析
在遞迴過程中，空間複雜度取決於樹的高度，最壞情況下為O(N)，在平衡二叉樹中為O(log N)。


解題思路
這個問題可以通過深度優先搜索（DFS）來解決。基本思路是遞迴地遍歷二叉樹，並在達到指定的深度時，添加新節點。具體步驟如下：

特殊情況處理：如果插入深度為1，則新節點將成為新的根節點，並將原有的根節點作為新根節點的左子節點。
遞迴遍歷：對於深度大於2的情況，對當前節點的左右子節點進行遞迴調用，每次調用時將深度減1。
插入節點：當達到深度為2時，將當前節點的左子節點和右子節點替換為新的節點，並將原來的左子節點和右子節點分別設置為新節點的左子節點和右子節點。
    """