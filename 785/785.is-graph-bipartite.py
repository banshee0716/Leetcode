#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#


# @lc code=start
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # 獲取圖中節點的數量
        n = len(graph)
        # 初始化每個節點的顏色為0
        colors = [0] * n

        # 遍歷每個節點
        for i in range(n):
            # 若該節點未被著色，則嘗試使用顏色1進行著色
            if colors[i] == 0:
                # 若該節點無法被著色，則返回False
                if not self.dfs(graph, colors, i, 1):
                    return False

        # 若所有節點均能被著色，則返回True
        return True

    def dfs(self, graph, colors, node, color):
        # 若該節點已被著色
        if colors[node] != 0:
            # 檢查其顏色是否與嘗試著色的顏色相同，相同則返回True，否則返回False
            return colors[node] == color

        # 將該節點著色
        colors[node] = color

        # 對該節點的每個鄰居節點進行相反顏色的著色，若有鄰居節點無法被著色，則返回False
        for neighbor in graph[node]:
            if not self.dfs(graph, colors, neighbor, -color):
                return False

        # 若該節點及其所有鄰居節點都能被正確著色，則返回True
        return True


"""
目標是判斷一個無向圖是否為二分圖。二分圖是一種圖，可以將所有的點劃分為兩個不相交的集合，使得每一條邊的兩個端點都分屬於不同的集合。以下是解題思路、程式碼註解以及時間和空間複雜度分析：

解題思路：
這個問題可以使用深度優先搜尋 (DFS) 或廣度優先搜尋 (BFS) 的方式來解決。
在這裡我們使用了深度優先搜尋的方法，用顏色來標記每一個點，
初始時每個點的顏色都為 0，然後從每個還未被著色的點出發，用 1 和 -1 兩種顏色來對點進行著色，如果在著色的過程中發現相鄰的兩個點顏色相同，則表示此圖不是二分圖。

"""


"""
時間複雜度：
此算法的時間複雜度為 O(n+e)，其中 n 是節點的數量，e 是邊的數量。我們需要遍歷每個節點和每條邊。

空間複雜度：
此算法的空間複雜度為 O(n)，因為我們需要一個長度為 n 的 colors 陣列來記錄每個節點的顏色。再者，由於使用了遞迴，還需要考慮棧空間的使用。在最壞情況下，DFS的遞迴深度可能達到 n。
"""
# @lc code=end
