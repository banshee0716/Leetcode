"""
1. 首先，我們初始化變量並找出起始點 '@' 的位置以及所有鑰匙的位置。

2. 接著，我們開始 BFS。每次從待訪問的隊列中取出一個點，然後試圖訪問其上下左右四個相鄰的點。

3.
- 如果相鄰的點是空地或者起始點，我們就直接訪問；
- 如果相鄰的點是鑰匙，我們就拿起鑰匙並訪問；
- 如果相鄰的點是門，我們就檢查我們是否有對應的鑰匙，如果有就打開門並訪問。

4. 在訪問過的點我們都會記錄下來，避免重複訪問。記錄的方式是將該點的座標和當前所持有的鑰匙狀態一起存入一個 set 當中。

5. 當我們有一個點的所有鑰匙和原本所有鑰匙相同時，我們就找到了解答。"""

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        # 如果地圖為空，返回 -1
        if not grid or not grid[0]:
            return -1
        
        # 獲取地圖的長度和寬度
        m, n = len(grid), len(grid[0])
        
        # 初始化所有鑰匙的狀態
        all_keys = [0, 0, 0, 0, 0, 0]
        
        # 尋找起始點和所有鑰匙
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    i_start, j_start = i, j
                elif grid[i][j].islower():
                    all_keys[ord(grid[i][j]) - ord('a')] = 1
        all_keys = tuple(all_keys)
        
        # 初始化 BFS 隊列和訪問集
        curr_level = [(i_start, j_start, tuple(6 * [0]))]
        visited = {(i_start, j_start, tuple(6 * [0]))}
        
        # 初始化移動次數
        moves = 0
        
        # 開始 BFS
        while curr_level:
            next_level = []
            for x, y, keys in curr_level:
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    r, c = x + dx, y + dy
                    if 0 <= r < m and 0 <= c < n and grid[r][c] != '#':
                        if grid[r][c] in '.@':
                            if (r, c, keys) not in visited:
                                visited.add((r, c, keys))
                                next_level.append((r, c, keys))
                        elif grid[r][c].islower():
                            new_keys = list(keys)
                            new_keys[ord(grid[r][c]) - ord('a')] = 1
                            new_keys = tuple(new_keys)
                            if new_keys == all_keys:
                                return moves + 1
                            if (r, c, new_keys) not in visited:
                                visited.add((r, c, new_keys))
                                next_level.append((r, c, new_keys))
                        else: # grid[r][c].isupper() == True
                            if keys[ord(grid[r][c].lower()) - ord('a')] == 1 and (r, c, keys) not in visited:
                                visited.add((r, c, keys))
                                next_level.append((r, c, keys))
            curr_level = next_level
            moves += 1
        return -1
    
    
"""
時間複雜度為 O(NM * 2^K)，其中 N, M 是地圖的行數和列數，K 是鑰匙的數量。最壞情況下，我們需要遍歷所有的格子，對於每個格子我們需要考慮所有鑰匙的狀態，所以時間複雜度為 O(NM * 2^K)。

空間複雜度也是 O(NM * 2^K)，因為我們需要儲存所有格子和鑰匙狀態的訪問狀態。
"""
