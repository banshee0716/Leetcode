class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        for i in range(1,len(A)):
            for j in range(len(A[0])):
		
            #edge cases are first column and last column which only have two paths from above
                if j == 0:
                    A[i][j]  = min((A[i][j] + A[i - 1][j]), (A[i][j] + A[i - 1][j + 1]) )
				
                elif (j == len(A[0]) - 1):
                    A[i][j]  = min((A[i][j] + A[i - 1][j]), (A[i][j] + A[i - 1][j - 1]) )
				
            #every other column will have three paths coming from above
                else:
                    A[i][j] = min(A[i][j] + A[i - 1][j],A[i][j] + A[i - 1][j + 1], A[i][j] + A[i - 1][j - 1])
        
	# Now that minimum falling sums for each value at the bottom row have been computer
	# We can just take the min of the bottow row to get the smallest overall path sum 
        return min(A[len(A) - 1])
    
    """
給定一個 n x n 整數矩陣數組，返回通過矩陣的任何下降路徑的最小和。

下降路徑從第一行中的任何元素開始，並選擇下一行中正下方或左/右對角線的元素。具體來說，位置 (row, col) 的下一個元素將為 (row + 1, col - 1)、(row + 1, col) 或 (row + 1, col + 1)。
    """