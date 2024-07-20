class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n, m = len(rowSum), len(colSum)
        matrix = [[0] * m for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                matrix[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= matrix[i][j]
                colSum[j] -= matrix[i][j]
        return matrix
        
        
    
    
    """
給定兩個非負整數數組 rowSum 和 colSum，其中 rowSum[i] 是第 i 行中的元素總和，colSum[j] 是 2D 矩陣的第 j 列中的元素總和。換句話說，您不知道矩陣的元素，但您確實知道每行和每列的總和。

找出大小為 rowSum.length x colSum.length 且滿足 rowSum 和 colSum 要求的任意非負整數矩陣。

傳回一個二維數組，表示滿足要求的任何矩陣。保證至少存在一個滿足要求的矩陣。
    """