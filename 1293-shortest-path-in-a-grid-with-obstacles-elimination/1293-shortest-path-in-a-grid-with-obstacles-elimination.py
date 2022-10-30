class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        if k >= m + n - 2:
            return m + n - 2# if we can go by manhattan distance -> let's go
        
        DIR = [0, 1, 0, -1, 0]
        q = deque([(0, 0, k)])  # pair of (r, c),用de
        seen = set()
        seen.add((0, 0, k))
        step = 0
        while q:
            for _ in range(len(q)):
                r, c, k = q.popleft()#定義現行步數
                if r == m - 1 and c == n - 1: 
                    return step  # Reach to the bottom right cell
                for i in range(4): #嘗試走向四個方向
                    nr, nc = r + DIR[i], c + DIR[i + 1]#模擬下的ˊ走法
                    if nr < 0 or nr == m or nc < 0 or nc == n: #如果跟過來是同一方向,CONTINUE
                        continue  # Skip out of bound cells!
                    newK = k - grid[nr][nc]#如果有的話,刪除現在的牆壁
                    newState = (nr, nc, newK)#更新狀態
                    if newK >= 0 and newState not in seen:
                        seen.add(newState)
                        q.append(newState)

            step += 1

        return -1
            
        
        
        
        
        
        
        #bfs