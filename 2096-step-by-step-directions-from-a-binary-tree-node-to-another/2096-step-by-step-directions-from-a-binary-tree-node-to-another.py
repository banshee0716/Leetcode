# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        def lca(node: Optional[TreeNode]) -> Optional[TreeNode]:
            """
            Find the lowest common ancestor (LCA) of start and dest nodes.
            """
            if not node or node.val in (startValue, destValue):
                return node
            left, right = lca(node.left), lca(node.right)
            return node if left and right else left or right

        # Find the LCA of start and dest nodes
        root = lca(root)  # We only need to consider this sub-tree

        ps = pd = ""  # Paths from LCA to start and dest nodes
        stack = [(root, "")]
        while stack:
            node, path = stack.pop()
            if node.val == startValue:
                ps = path
            if node.val == destValue:
                pd = path
            if node.left:
                stack.append((node.left, path + "L"))
            if node.right:
                stack.append((node.right, path + "R"))

        # Construct the final path:
        # 1. Go up from start to LCA: "U" * len(ps)
        # 2. Then follow the path from LCA to dest: pd
        return "U" * len(ps) + pd
    
    """
這個解決方案採用了兩步驟的方法來解決問題:

首先,找到起始節點和目標節點的最低共同祖先(LCA)。
然後,從LCA分別找到到起始節點和目標節點的路徑。

具體步驟如下:
a) 使用遞歸方法找到LCA。這個方法非常巧妙,能夠在一次遍歷中找到LCA。
b) 一旦找到LCA,我們就只需要考慮以LCA為根的子樹,這大大減少了需要搜索的節點數量。
c) 使用深度優先搜索(DFS)來找到從LCA到起始節點和目標節點的路徑。這裡使用了堆疊來實現迭代式DFS。
d) 最後,將從LCA到起始節點的路徑轉換為向上移動("U"),再加上從LCA到目標節點的路徑,就得到了最終的路徑。

時間複雜度:

O(N),其中N是樹中的節點數。
找LCA需要O(N)時間。
在最壞情況下,DFS也需要遍歷所有節點,也是O(N)。
因此,總體時間複雜度為O(N)。

空間複雜度:

O(H),其中H是樹的高度。
在最壞情況下(樹退化為鏈表時),空間複雜度為O(N)。
lca函數的遞歸調用棧最多使用O(H)空間。
DFS使用的堆疊在最壞情況下也使用O(H)空間。
因此,總體空間複雜度為O(H),最壞情況下為O(N)。
    """