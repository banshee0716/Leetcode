# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        
        children = set()
        m = {}
        for p,c,l in descriptions:
            np = m.setdefault(p, TreeNode(p))
            nc = m.setdefault(c, TreeNode(c))
            if l:
                np.left = nc
            else:
                np.right = nc
            children.add(c)
        root = (set(m) - set(children)).pop()
        return m[root]
    
    
"""
給定一個 2D 整數陣列描述，其中 descriptions[i] = [parenti, childi, isLefti] 表示在唯一值的二元樹中，parenti 是 childi 的父級。此外，

如果 isLefti == 1，則 childi 是 Parenti 的左孩子。
如果 isLefti == 0，則 childi 是 Parenti 的右孩子。
構造由描述描述的二元樹並返回其根。

將產生測試用例以使二元樹有效。
"""