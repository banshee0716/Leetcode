# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        # 使用集合對要刪除的節點進行快速查找
        to_delete_set = set(to_delete)
        res = []  # 存儲結果的列表

        def helper(root, is_root):
            # 如果當前節點為空，則返回None
            if not root:
                return None
            
            # 檢查當前節點是否需要被刪除
            root_deleted = root.val in to_delete_set

            # 如果當前節點是根且未被刪除，將其添加到結果中
            if is_root and not root_deleted:
                res.append(root)

            # 遞迴地處理左右子節點，並更新其指向
            root.left = helper(root.left, root_deleted)
            root.right = helper(root.right, root_deleted)

            # 如果當前節點被刪除，返回None，否則返回當前節點
            return None if root_deleted else root

        # 開始DFS遞迴
        helper(root, True)
        return res

        
"""
解題思路:

1.將需要刪除的節點存放到一個集合中，以便於快速地查找是否一個節點需要被刪除。
2.使用DFS深度優先搜索的方式遞迴地探索每個節點。
3.對於當前的節點，我們需要確定是否它是一個新樹的根節點。
4.如果一個節點被刪除了，那麼它的子節點都將成為新樹的根，除非那些子節點也被刪除。

時間複雜度: O(n)，其中n是樹中的節點數量。每個節點都被訪問一次。

空間複雜度: O(n)。這主要是因為遞迴堆疊的深度、結果列表和需要刪除的節點集合。
"""