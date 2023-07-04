class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        # 定義 DFS 函數，用來探索從某一個點開始的最長遞增路徑
        def dfs(i, j):
            # 如果 dp[i][j] 已經被計算過，則直接返回結果
            if not dp[i][j]:
                val = matrix[i][j]
                # 使用 max 函數找出從四個方向移動後的最大路徑長度，並加上當前的點
                dp[i][j] = 1 + max(
                    dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                    dfs(i + 1, j) if i < M - 1 and val > matrix[i + 1][j] else 0,
                    dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                    dfs(i, j + 1) if j < N - 1 and val > matrix[i][j + 1] else 0)
            return dp[i][j]

        # 如果矩陣為空，則返回 0
        if not matrix or not matrix[0]: return 0
        M, N = len(matrix), len(matrix[0])  # 獲取矩陣的行數和列數
        dp = [[0] * N for i in range(M)]  # 初始化 DP 表
        # 對矩陣中的每一個點，調用 DFS 函數，並找出最長的遞增路徑
        return max(dfs(x, y) for x in range(M) for y in range(N))

"""
時間複雜度為 O(mn)，其中 m 和 n 分別為矩陣的行數和列數，這是因為我們需要對矩陣中的每一個點進行深度優先搜索。
空間複雜度也為 O(mn)，因為我們需要用一個和輸入矩陣等大小的 DP 表來保存中間結果。
"""