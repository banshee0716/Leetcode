from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # 創建鄰接列表表示圖
        adj = defaultdict(list)

        # 建立雙向的邊
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(i):
            # 將節點添加到當前的組件中
            component.add(i)
            # 遍歷該節點的所有子節點
            for child in adj[i]:
                # 如果子節點尚未被訪問，則進行DFS搜索
                if child not in visited:
                    visited.add(child)
                    dfs(child)

        ans = 0
        # 記錄已訪問的節點
        visited = set()

        # 遍歷所有節點
        for i in range(n):
            # 如果該節點尚未被訪問
            if i not in visited:
                # 創建一個新的組件來存儲當前連接組件中的節點
                component = set()
                visited.add(i)
                # 進行DFS搜索
                dfs(i)
                # 檢查此組件是否為完整的連接組件
                if all(len(adj[node]) == len(component) - 1 for node in component):
                    ans += 1

        return ans
        
"""
解題思路：

首先，我們使用鄰接列表來表示圖。
我們使用深度優先搜索(DFS)來找到所有連接組件。
對於每個連接組件，我們檢查它是否是一個完整的連接組件。這是通過確保每個節點的所有鄰居都在該組件內來完成的。
時間複雜度：O(N + E)，其中N是節點的數量，E是邊的數量。這是因為我們可能需要訪問所有的節點和邊。

空間複雜度：O(N + E)，主要是因為我們存儲了每個節點的邊和用於深度優先搜索的調用堆棧。"""