from collections import defaultdict, deque
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        # 建立鄰接表和每個節點的度數
        adjacency_list = defaultdict(list)
        degree = [0] * n
        for u, v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
        # 初始化葉子節點隊列
        leaves = deque([i for i in range(n) if degree[i] == 1])
        
        # 循環去除葉子節點，直到剩下2個或更少的節點
        remaining_nodes = n
        while remaining_nodes > 2:
            leaves_count = len(leaves)
            remaining_nodes -= leaves_count
            for _ in range(leaves_count):
                leaf = leaves.popleft()
                for neighbor in adjacency_list[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        leaves.append(neighbor)
        
        return list(leaves)
"""
解題思路
此問題可以透過去葉子節點的方式來解決，即逐步剝離每層的葉子節點，直到剩下中心節點。這種方法基於一個觀察，即從外圍向中心收縮可以幫助快速定位到可能的根節點，這些根節點能夠產生最小高度的樹。

建立鄰接表與節點度數：首先使用邊列表建立每個節點的鄰接表，並計算每個節點的度數。
初始化葉子節點隊列：節點度數為1的即為葉子節點，將它們加入到隊列中。
逐層剝離葉子節點：每次循環剝離一層葉子節點，更新其鄰居的度數，若鄰居度數變為1則成為新的葉子節點。
終止條件：當剩餘節點數小於或等於2時，這些節點即為所有可能的根節點。
"""