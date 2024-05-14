class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])  # 獲取矩陣的行和列數
        DIR = [0, 1, 0, -1, 0]  # 方向陣列，用於簡化上下左右移動
        
        def dfs(r, c):
            # 確保當前位置有效，且有金礦可採
            if r < 0 or r == m or c < 0 or c == n or grid[r][c] == 0:
                return 0
            ans = 0
            orgGold = grid[r][c]  # 保存當前位置金礦數
            grid[r][c] = 0  # 採集完當前位置的金礦
            
            # 探索四個方向
            for i in range(4):
                ans = max(ans, dfs(r + DIR[i], c + DIR[i+1]))
            
            grid[r][c] = orgGold  # 恢復當前位置金礦數
            return ans + orgGold  # 返回包括當前位置的總金礦數
        
        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:  # 只有當前位置有金礦時才開始DFS
                    ans = max(ans, dfs(r, c))
        
        return ans

    
    """
題目描述
給定一個二維矩陣 grid，每個單元格含有不同數量的金礦，0表示沒有金礦。你可以從任何有金礦的單元格出發，向上下左右四個方向移動，直到走到沒有金礦的單元格或邊界為止。每次經過一個單元格，你會收集所有的金礦，並且該單元格的金礦變為0。該怎麼走，才能收集到最多的金礦？

解題思路
1. 深度優先搜索 (DFS)：從每個含有金礦的單元格開始，使用DFS探索所有可能的路徑並收集金礦。
2. 避免重複走訪：在進行DFS前，將當前單元格設置為0以防止重複走訪，DFS完成後恢復原始金礦數以供其他路徑使用。
3. 全局最大值：維護一個全局最大值變量，每次DFS返回時，檢查是否需要更新此最大值。


時間複雜度：O(m * n * 4^k)，其中 m 和 n 分別為矩陣的行數和列數，k 為進行DFS的最大深度。每次DFS最多探索4個方向。
空間複雜度：O(m * n)，主要消耗於遞迴棧空間，最壞情況下遞迴深度可能達到 m * n。

    """