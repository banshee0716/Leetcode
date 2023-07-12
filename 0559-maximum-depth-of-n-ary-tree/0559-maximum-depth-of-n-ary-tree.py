"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:  # 如果樹為空，則其深度為 0
            return 0

        depth = 0  # 初始化樹的深度
        nodes_queue = [root]  # 將根節點加入隊列
        next_nodes_queue = []  # 初始化下一層節點的隊列

        while nodes_queue:  # 當隊列非空時
            node_out = nodes_queue.pop(0)  # 從隊列中取出一個節點
            for child in node_out.children:  # 將該節點的所有子節點加入下一層節點的隊列
                next_nodes_queue.append(child)
            if not nodes_queue:  # 如果當前層的所有節點都已經訪問完畢
                nodes_queue, next_nodes_queue = next_nodes_queue, nodes_queue  # 將下一層節點的隊列轉移到當前層，並清空下一層節點的隊列
                depth += 1  # 樹的深度加 1

        return depth  # 返回樹的最大深度

"""
時間複雜度是 O(N)，其中 N 是樹中的節點數量，因為我們需要訪問每個節點。
空間複雜度也是 O(N)，用於存儲隊列。
"""