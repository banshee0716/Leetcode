class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        # 初始化每一行和每一列的最大值
        rows_max = [0] * len(grid)
        cols_max = [0] * len(grid[0])

        # 找出每一行和每一列的最大值
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                rows_max[i] = max(rows_max[i], grid[i][j])
                cols_max[j] = max(cols_max[j], grid[i][j])

        # 初始化增加的總高度
        res = 0

        # 對於每一個樓房，找出能增加的最大高度，並將其加入總和
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res += min(rows_max[i], cols_max[j]) - grid[i][j]

        # 返回增加的總高度
        return res
    
"""
在不改變城市的外觀的情況下（即從任何方向看，都不能看出高度的增加），使得城市的高度增加最大。我們可以通過以下步驟來解決這個問題：

1. 首先，找出每行和每列的最大值，這將確定這個位置的樓房可以增加的最大高度。
2. 接著，對於每一個樓房，我們將它增加到該位置的行最大值和列最大值中較小的一個，這樣就能確保不會改變城市的外觀。
3. 最後，將所有增加的高度加起來，就是我們的答案。

對於時間複雜度，由於我們需要遍歷整個陣列兩次，所以時間複雜度為O(n^2)，其中n為陣列的長度。
對於空間複雜度，我們需要存儲每一行和每一列的最大值，所以空間複雜度為O(n)。
"""