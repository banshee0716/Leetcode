#
# @lc app=leetcode id=1466 lang=python3
#
# [1466] Reorder Routes to Make All Paths Lead to the City Zero
#

# @lc code=start
import collections


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.res = 0  # 用來計算改變方向的次數
        roads = set()  # 存儲已經存在的道路
        graph = collections.defaultdict(list)  # 使用 defaultdict 創建一個無向圖
        for u, v in connections:
            roads.add((u, v))
            graph[v].append(u)  # 存儲有向邊
            graph[u].append(v)

        def dfs(u, parent):
            self.res += (parent, u) in roads  # 當從 parent 到 u 的道路不存在時，將其加入到 res 中
            for v in graph[u]:
                if v == parent:
                    continue
                dfs(v, u)  # 對所有子節點進行深度優先搜索

        dfs(0, -1)
        return self.res


"""
時間複雜度：
O(n)，其中 n 是節點的數量。在最壞的情況下，我們可能需要訪問所有的節點，因此時間複雜度是 O(n)。

空間複雜度：
O(n+m)，其中 n 是節點的數量，m 是邊的數量。我們需要存儲圖形，其大小是 O(n+m)，並且需要使用遞歸堆棧來保持深度優先搜索的運行，其大小最多是 O(n)。因此，空間複雜度是 O(n+m)。
"""
# @lc code=end
