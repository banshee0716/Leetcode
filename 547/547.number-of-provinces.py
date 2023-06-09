#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#

# @lc code=start
""" 
這道題目是找出無向圖中的連通分量數量。每個城市都與其他城市連通或者不連通，我們需要找出有多少個獨立的省份（即連通分量）。

這段程式碼採用深度優先搜索 (DFS) 的方法。
首先，初始化訪問陣列 visited 為 False。
接著，遍歷每一個城市，如果該城市未被訪問過，則增加省份數量，並對該城市進行深度優先搜索，將所有與該城市直接或間接相連的城市都標記為已訪問。
最後，返回省份的數量。
"""


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        provinces = 0
        visited = [False] * n

        def dfs(node):
            # 將訪問過的節點標記為 True
            visited[node] = True
            # 遍歷該節點的所有鄰居，如果與鄰居之間有邊，且該鄰居未被訪問過，則遞迴訪問鄰居
            for neighbor in range(n):
                if isConnected[node][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)

        for i in range(n):
            # 如果城市 i 未被訪問過，則其為一個新的省份
            if not visited[i]:
                provinces += 1
                # 對城市 i 進行深度優先搜索，標記所有與其直接或間接相連的城市
                dfs(i)

        # 返回省份的數量
        return provinces


""" 

時間複雜度：
O(n^2)，其中 n 是城市的數量。在最壞的情況下，需要遍歷矩陣中的每一個元素。

空間複雜度：
O(n)，其中 n 是城市的數量。這主要來自於遞迴棧和 visited 陣列的空間需求。
"""
# @lc code=end
