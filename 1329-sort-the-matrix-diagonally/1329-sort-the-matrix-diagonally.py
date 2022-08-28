class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        diagonals = defaultdict(list) 
        
        for i in range(n):
            for j in range(m):
                diagonals[i-j].append(mat[i][j])
        
        for k in diagonals:
            diagonals[k].sort(reverse = True)
        
        
        for i in range(n):
            for j in range(m):
                mat[i][j] = diagonals[i-j].pop()
        
        return mat