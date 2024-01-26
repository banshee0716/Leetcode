class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
		# define the dp array
        dp = [[[-1]*(maxMove+1) for _ in range(n+1)] for _ in range(m+1)]
        
        def solve(i, j, maxMove):
            if maxMove < 0:
                return 0
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            
			# if the dp array at this position contains some value(not -1) then it means it has been computed earlier
			# so we don't need to compute again, hence return whatever value is present in dp.
            if dp[i][j][maxMove] != -1:
                return dp[i][j][maxMove]
            
			# otherwise compute the value
            a = solve(i-1, j, maxMove - 1)
            b = solve(i+1, j, maxMove - 1)
            c = solve(i, j-1, maxMove - 1)
            d = solve(i, j+1, maxMove - 1)
            
			# store the computed value in dp array so that we do not need to compute it again when the same input occurs again.
            dp[i][j][maxMove] = a + b + c + d
            return dp[i][j][maxMove]
        
        return solve(startRow, startColumn, maxMove) % 1000000007
    
    """
有一個 m x n 的網格，裡面有一個球。球最初位於位置 [startRow, startColumn]。您可以將球移動到網格中四個相鄰單元格之一（可能跨越網格邊界超出網格）。您最多可以對球套用 maxMove 移動。

給定五個整數 m、n、maxMove、startRow、startColumn，傳回將球移出網格邊界的路徑數。由於答案可能非常大，因此傳回 109 + 7 求模的結果。
    """