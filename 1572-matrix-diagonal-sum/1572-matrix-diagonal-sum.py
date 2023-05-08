class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        mid = n // 2
        summation = 0
        for i in range(n):
            summation += mat[i][i]
            summation += mat[n-1-i][i]
        
        if n % 2 == 1:
            summation -= mat[mid][mid]
            
        return summation
                