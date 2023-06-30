class DSU:
    def __init__(self, N):
        # 初始化父節點列表
        self.p = list(range(N))

    def find(self, x):
        # 如果x不是自己的父節點，則將x的父節點設置為x的父節點的父節點，然後回傳x的父節點
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        # 將x的根節點與y的根節點連接
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr

class Solution:
    def latestDayToCross(self, n, m, C):
        # 初始化並查集，二維網格和鄰居列表
        dsu = DSU(m*n + 2)
        grid = [[1] * m for _ in range(n)]
        neibs = [[0,1],[0,-1],[1,0],[-1,0]]

        # 將每個淹沒位置的座標調整為0-indexed
        C = [(x-1, y-1) for x, y in C]

        def index(x, y):
            # 將二維座標轉換為一維座標
            return x * m + y + 1

        for i in range(len(C) - 1, -1, -1):
            x, y = C[i][0], C[i][1]

            # 將淹沒的位置標記為乾燥
            grid[x][y] = 0

            # 將該位置與其乾燥的鄰居位置進行合併
            for dx, dy in neibs:
                ind = index(x+dx, y+dy)
                if x+dx>=0 and x+dx<n and y + dy >= 0 and y + dy < m and grid[x+dx][y+dy] == 0:
                    dsu.union(ind, index(x, y))

            # 如果該位置在第一行或最後一行，將其與起點或終點進行合併
            if x == 0:
                dsu.union(0, index(x, y))
            if x == n - 1:
                dsu.union(m*n + 1, index(x, y))

            # 檢查起點與終點是否連通，如果連通，返回當前的天數
            if dsu.find(0) == dsu.find(m*n + 1):
                return i

            
"""
1. 首先，我們定義一個 DSU 類別來實現並查集的基本操作：查找和合併。查找操作用於找出某一元素所在的集合，合併操作則用於將兩個元素所在的集合合併為一個。
2. 在解題函數 latestDayToCross 中，我們首先初始化一個 DSU 實例，以及一個二維矩陣 grid 來儲存每個位置是否被洪水淹沒。
3. 接著，我們從最後一天開始反向遍歷，對於每一天，我們先將該天的淹沒位置標記為乾燥，然後嘗試將該位置與其乾燥的鄰居位置合併。
4. 如果該位置在第一行，我們就將其與起點合併；如果該位置在最後一行，我們就將其與終點合併。
5. 最後，我們檢查起點與終點是否連通，如果連通，則返回當前的天數。這是因為在反向遍歷的過程中，一旦起點與終點連通，那麼在之後的天數中，起點和終點只會保持連通或者因為新的淹沒位置而變得不連通，因此當起點和終點首次連通的那一天，就是我們可以通過矩陣的最晚一天。
"""
"""
O(mn + C*alpha(mn))
"""