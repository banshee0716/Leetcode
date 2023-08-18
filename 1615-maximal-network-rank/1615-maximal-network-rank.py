from typing import List

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # 創建一個字典來存儲每個城市與其相鄰城市之間的關係
        graph = {}
        
        # 填充圖形結構
        for u, v in roads:
            graph.setdefault(u, set()).add(v)
            graph.setdefault(v, set()).add(u)
        
        # 初始化答案為0
        ans = 0
        
        # 遍歷每一對城市
        for i in range(n): 
            for j in range(i+1, n):
                # 計算網路評級
                val = len(graph.get(i, set())) + len(graph.get(j, set())) - (j in graph.get(i, set()))
                # 更新最大值
                ans = max(ans, val)
        
        # 返回最大網路評級
        return ans

        
"""

以下是解題思路：

1. 首先使用一個字典 graph 來建立每個城市與其相鄰城市之間的關係。
2. 通過遍歷所有的道路來填充這個 graph。
3. 然後對每一對城市 (i, j)，計算他們的網路評級，這可以通過將它們相鄰的城市數量加起來得到。但如果他們之間存在直接的道路，則減去1。
4. 更新最大網路評級。
返回最大的網路評級。

時間複雜度: O(n^2)。這裡 n 是城市的數量，因為我們需要考慮每一對城市。

空間複雜度: O(n + r)。這裡 r 是 roads 的長度。因為我們使用了一個字典來存儲每個城市的相鄰城市。
"""