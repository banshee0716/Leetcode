#
# @lc app=leetcode id=2101 lang=python3
#
# [2101] Detonate the Maximum Bombs
#

# @lc code=start
""" 
我們將每個炸彈看作一個節點，如果一個炸彈的爆炸範圍包含了另一個炸彈，那麼就在這兩個炸彈之間畫一條邊。
在這樣的圖形中，我們的目標就是找出最大的連通子圖。
"""


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n, max_bombs, graph = len(bombs), 0, defaultdict(list)

        # 構建圖，每個炸彈是一個節點，如果炸彈i可以引爆炸彈j，則在節點i和j之間添加邊
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if (
                    bombs[i][2] ** 2
                    >= (bombs[i][0] - bombs[j][0]) ** 2
                    + (bombs[i][1] - bombs[j][1]) ** 2
                ):
                    graph[i] += [j]

        # 定義深度優先搜索函數，遍歷節點的所有子節點
        def dfs(node, visited):
            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    dfs(child, visited)

        # 對每個節點進行深度優先搜索，並更新連接節點的最大數量
        for i in range(n):
            visited = set([i])
            dfs(i, visited)
            max_bombs = max(max_bombs, len(visited))

        return max_bombs  # 返回連接節點的最大數量


"""

時間複雜度：O(n^2)，
其中 n 是炸彈的數量。在最壞的情況下，我們需要遍歷所有的炸彈並對每一個炸彈進行深度優先搜索。

空間複雜度：O(n)，
其中 n 是炸彈的數量。在最壞的情況下，我們可能需要訪問網格中的所有單元格，且訪問信息需要儲存在visited集合中。
"""
# @lc code=end
