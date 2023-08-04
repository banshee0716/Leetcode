class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        d = defaultdict(list)
        
        for i, j in product(range(len(grid)),        
                            range(len(grid[0]))):
            
            d[i-j].append((i,j))
        
        for diag in d:
            arr = [grid[i][j] for i,j in d[diag]]       # <-- Construct an arr of the elements
                                                        #     on the diagonal.

            for idx, (i,j) in enumerate(d[diag]):       # <-- Overwrite each element in the diagonal.   
                grid[i][j] = abs(len(set(arr[:idx])) -  #     in the array with its score.
                                 len(set(arr[idx+1:])))
            
        return grid                                     # <-- Return the overwritten 'grid' as the
                                                        #     'answer' matrix.
        
        
        
"""
給定一個大小為 m x n 的 0 索引二維網格，您應該找到大小為 m x n 的矩陣答案。

矩陣答案的每個單元格 (r, c) 的值按以下方式計算：

令 topLeft[r][c] 為矩陣網格中單元格 (r, c) 左上角對角線中不同值的數量。
令 BottomRight[r][c] 為矩陣網格中單元格 (r, c) 右下對角線中不同值的數量。
然後answer[r][c] = |topLeft[r][c] - BottomRight[r][c]|。

返回矩陣answer。

矩陣對角線是單元格的對角線，從最頂行或最左列中的某個單元格開始，沿右下方向延伸，直到到達矩陣的末尾。

如果單元格 (r1, c1) 屬於同一對角線且 r1 < r，則單元格 (r1, c1) 屬於單元格 (r, c) 的左上角對角線。同樣定義右下對角線。
"""