class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagic(i, j):
            once=[False]*10
            rowSum=[0]*3
            colSum= [0]*3

            for a in range(i-1, i+2):
                for b in range(j-1, j+2):
                    x= grid[a][b]
                    if x < 1 or x > 9: return False
                    rowSum[a-i+1] += x
                    colSum[b-j+1] += x
                    if once[x]: 
                        return False  # it's not unique
                    once[x]=True

            for b in once[1:]: 
                if not b: return False

            for sum in rowSum:
                if sum!=15: return False
            for sum in colSum:
                if sum!=15: return False
            
            return grid[i-1][j-1]+grid[i+1][j+1]==10 and grid[i+1][j-1]+grid[i-1][j+1]==10
        
        r, c = len(grid), len(grid[0])
        if r < 3 or c < 3: 
            return 0

        cnt=0
        for i in range(1, r-1):
            for j in range(1, c-1):
                if grid[i][j] == 5 and isMagic(i, j): 
                    cnt+=1
        return cnt



        
    """
3 x 3 幻方是一個 3 x 3 的網格，其中填充了從 1 到 9 的不同數字，使得每行、每列和兩條對角線都具有相同的總和。

給定一個 row x col 整數網格，有多少 3 x 3 連續幻方子網格？

注意：魔術方塊只能包含 1 到 9 的數字，而網格最多可以包含 15 個數字。
    """