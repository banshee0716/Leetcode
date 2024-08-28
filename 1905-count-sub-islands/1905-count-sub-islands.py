class Solution:
    def check_islands(self, grid1, grid2, row, col):
        #條件爆掉
        if row < 0 or row >= len(grid2) or col < 0 or col >= len(grid2[0]) or grid2[row][col] == 0: 
            return True
        elif (grid1[row][col] == 1 and grid2 [row][col] == 0) or (grid1[row][col] == 0 and grid2 [row][col] == 1):
            return False
        elif (grid1[row][col] == 1 and grid2 [row][col] == 1):
            grid2[row][col] = 0
            
            left = self.check_islands(grid1, grid2, row, col - 1)
            right = self.check_islands(grid1, grid2, row, col + 1)
            top = self.check_islands(grid1, grid2, row - 1, col)
            bottom = self.check_islands(grid1, grid2, row + 1, col)
            
            return left and right and top and bottom
        
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        nums_islands = 0
        for row in range(len(grid2)):
            for col in range(len(grid2[row])):
                if (grid2[row][col] == 1) and self.check_islands(grid1, grid2, row, col):
                    nums_islands += 1
        
        return nums_islands
            
        
            