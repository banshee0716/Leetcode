class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m,n = len(grid), len(grid[0])
        
        prefix, suffix = [1], [1]
        for i in range(m):
            for j in range(n):
                prefix.append((prefix[-1] * grid[i][j]) % 12345)
        
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                suffix.append((suffix[-1] * grid[i][j]) % 12345)
        
        for i,j in product(range(m), range(n)):
            k = i * n + j
            grid[i][j] = (prefix[k] * suffix[-k-2]) % 12345
        
        return grid
                
    """
給定0個索引的2D整數矩陣網格尺寸n * m，如果滿足以下條件：
    每個元素p [i] [j]被計算為除元素網格[i] [j]以外的所有元素的乘積。然後將該產品採用Modulo 12345。
    
返回網格的產品矩陣。
    """