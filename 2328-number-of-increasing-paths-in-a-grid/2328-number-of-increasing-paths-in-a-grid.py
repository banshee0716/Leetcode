class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        di, dj, mod, ans = 1, 0, 1000000007, 0
        R, C = range(len(grid)), range(len(grid[0]))
    
        @lru_cache(None)                            # <-- cache the results in recursion
        def dfs(i,j):                               
            nonlocal di, dj
            res = 0
            for _ in range(4):
                I, J, di, dj = i+di, j+dj, dj, -di  # <-- explores through neighbors
                if (I in R and J in C and 
                    grid[I][J] > grid[i][j]):
                    res+= dfs(I,J)      
            return (1+res)%mod

        for i in R:                                  # <-- iterates through the 2D array
            for j in C:                              #     and sums the counts of seq's
                ans+= dfs(i,j)
        return  ans%mod