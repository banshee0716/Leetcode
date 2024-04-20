class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def dfs(x, y):
            stack = [(x, y)]
            min_row, min_col = x, y
            max_row, max_col = x, y
            visited.add((x, y))
            
            while stack:
                cur_x, cur_y = stack.pop()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 探索四個方向
                    nx, ny = cur_x + dx, cur_y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and land[nx][ny] == 1:
                        visited.add((nx, ny))
                        stack.append((nx, ny))
                        min_row = min(min_row, nx)
                        min_col = min(min_col, ny)
                        max_row = max(max_row, nx)
                        max_col = max(max_col, ny)
            
            return (min_row, min_col, max_row, max_col)
        
        rows, cols = len(land), len(land[0])
        visited = set()
        result = []
        
        for i in range(rows):
            for j in range(cols):
                if land[i][j] == 1 and (i, j) not in visited:
                    min_row, min_col, max_row, max_col = dfs(i, j)
                    result.append([min_row, min_col, max_row, max_col])
        
        return result

    """
    
解題思路
這個問題可以透過深度優先搜索（DFS）解決，目的是為了識別矩陣中相連的1的集合（農田）。為了追蹤已訪問過的農田，使用一個visited集合來存儲已訪問過的座標。對於矩陣中的每個元素，如果其值為1且未被訪問過，則從該座標開始進行DFS，以識別整個連接的農田區域，並計算其邊界。

深度優先搜索（DFS）：從一個農田單元開始，探索所有相鄰的農田單元，並記錄訪問過的座標。同時，更新農田區域的最小和最大行列座標。
邊界記錄：每次找到一塊新的農田時，記錄其左上角和右下角的座標。

時間複雜度分析
整體過程中，每個單元最多被訪問一次，因此時間複雜度為O(N * M)，其中N和M分別是矩陣的行數和列數。

空間複雜度分析
visited集合的空間複雜度為O(N * M)
    """