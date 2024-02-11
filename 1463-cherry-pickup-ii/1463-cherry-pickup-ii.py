from typing import List

class Solution:
    def __init__(self):
        self.dy = [0, -1, 1]
        self.memo = [[[-1] * 71 for _ in range(71)] for _ in range(71)]

    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for arr2D in self.memo:
            for arr1D in arr2D:
                for i in range(n):
                    arr1D[i] = -1
        return self.dfs(grid, 0, 0, n - 1, m, n)

    def dfs(self, grid, i, c1, c2, m, n):
        if i == m:
            return 0
        if c1 < 0 or c2 < 0 or c1 >= n or c2 >= n:
            return float('-inf')
        if self.memo[i][c1][c2] != -1:
            return self.memo[i][c1][c2]

        ans = 0
        for k in range(3):
            for r in range(3):
                ans = max(ans, self.dfs(grid, i + 1, c1 + self.dy[k], c2 + self.dy[r], m, n))

        ans += grid[i][c1] if c1 == c2 else grid[i][c1] + grid[i][c2]
        self.memo[i][c1][c2] = ans
        return ans

    
    """
LeetCode 1463題「採櫻桃 II」要求在一個m x n的網格中，有兩個機器人從第一行的任意兩個位置開始，同時向下移動到最後一行，並且每一步都可以選擇向下或向下左或向下右移動。目標是找到一條路徑，使得兩個機器人能夠採集到最多的櫻桃。機器人不能移動到網格外，且當兩個機器人選擇同一個格子時，該格子的櫻桃只能被採集一次。

解題思路
動態規劃與深度優先搜索（DFS）：
    -使用一個三維數組memo[i][c1][c2]來存儲從第i行，第一個機器人在c1列，第二個機器人在c2列開始，能採集到的最多櫻桃數量。

DFS函數：
    -dfs(grid, i, c1, c2, m, n)函數嘗試從第i行、第一個機器人在c1列、第二個機器人在c2列開始，採集櫻桃並返回最大值。

邊界條件：
    -如果機器人移出網格範圍，則該路徑不可取，返回負無窮。
    -如果達到最後一行，則返回當前行的櫻桃數。

狀態轉移：
    -考慮機器人下一步的所有可能移動，更新答案為這些移動中能採集到的最多櫻桃數量。

記憶化：
    -為了避免重複計算，使用memo數組來存儲已計算過的結果。

時間複雜度
總時間複雜度為O(m * n * n * 9)，其中m和n分別為網格的行數和列數。每一層遞歸考慮9種不同的移動情況。

空間複雜度
空間複雜度為O(m * n * n)，用於存儲memo數組。
    """