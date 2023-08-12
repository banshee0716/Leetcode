class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 檢查網格的邊界和起始位置是否有障礙物
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0] == 1:
            return 0
        
        # 獲取網格的行和列數
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # 初始化兩個一維陣列來儲存每行的路徑數
        previous = [0] * n
        current = [0] * n
        # 設置起始位置的路徑數為1
        previous[0] = 1
        
        for i in range(m):
            # 對於第i行，第0列的位置，如果有障礙物，路徑數為0，否則路徑數與上一行相同
            current[0] = 0 if obstacleGrid[i][0] == 1 else previous[0]
            
            # 計算其他位置的路徑數
            for j in range(1, n):
                # 如果這個位置有障礙物，路徑數為0
                # 否則，路徑數是左側位置和上側位置的路徑數之和
                current[j] = 0 if obstacleGrid[i][j] == 1 else current[j-1] + previous[j]
            
            # 更新previous為當前行的路徑數
            previous[:] = current
        
        # 最後一個位置的路徑數就是答案
        return previous[n-1]
    
    
    """
    
解題思路：

1.	我們用兩個一維陣列來儲存每一行的路徑數，一個儲存上一行的路徑數，一個儲存當前行的路徑數。

2.	當前位置的路徑數是其左側和上側位置的路徑數之和，但如果當前位置有障礙物，路徑數為0。

時間複雜度：O(m * n)，因為我們需要遍歷整個網格一次。
空間複雜度：O(n)，我們使用了兩個一維陣列來儲存路徑數，所以空間複雜度是O(n)。
    """