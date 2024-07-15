# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional, Dict
from collections import defaultdict

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # Set to store all child nodes
        children = set()
        # Dictionary to store TreeNode objects, with default creation of new nodes
        node_map: Dict[int, TreeNode] = defaultdict(lambda: TreeNode(0))

        # Process each description to build the tree
        for parent, child, is_left in descriptions:
            # Get or create TreeNode objects for parent and child
            parent_node = node_map[parent]
            child_node = node_map[child]

            # Set the correct value for the nodes
            parent_node.val = parent
            child_node.val = child

            # Connect child to parent based on is_left flag
            if is_left:
                parent_node.left = child_node
            else:
                parent_node.right = child_node

            # Add child to the set of children
            children.add(child)

        # Find the root by getting the node that is not a child of any other node
        root_value = (set(node_map.keys()) - children).pop()

        # Return the root TreeNode
        return node_map[root_value]
        
    
"""
使用棧來處理嵌套的括號結構。每個棧元素是一個字典，用於存儲當前層級的原子計數。
遍歷化學式字符串，根據不同的字符類型進行相應的處理：
a. 遇到左括號 '('，創建新的字典並推入棧中。
b. 遇到右括號 ')'，處理括號內的原子計數，並將結果合併到上一層。
c. 遇到原子名稱，解析原子名稱和數量，更新當前字典。
最後，對結果進行排序並格式化輸出。

時間複雜度：

O(N * log(N))，其中 N 是化學式的長度。
遍歷化學式需要 O(N) 時間。
最後的排序操作需要 O(K * log(K)) 時間，其中 K 是不同原子的數量（最壞情況下 K = N/2）。
因此，總體時間複雜度為 O(N * log(N))。

空間複雜度：

O(N)，其中 N 是化學式的長度。
在最壞情況下（深度嵌套的括號），棧可能包含 O(N) 個元素。
每個 Counter 對象最多包含 O(N) 個元素。
因此，總體空間複雜度為 O(N)。
"""