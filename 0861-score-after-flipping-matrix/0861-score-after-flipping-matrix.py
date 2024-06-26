class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])  # 獲取行和列的數量
        res = (1 << (m - 1)) * n  # 所有行的最左側列貢獻的分數

        # 從第二列開始，考慮翻轉每一列
        for j in range(1, m):
            col_count = 0  # 紀錄此列中1的數量

            # 統計此列中與第一列相同元素的數量，即翻轉行後的1的數量
            for i in range(n):
                if grid[i][j] == grid[i][0]:
                    col_count += 1

            # 取此列1的數量與其補數的較大者，因為可以選擇是否翻轉整列
            max_ones = max(col_count, n - col_count)
            res += max_ones * (1 << (m - 1 - j))

        return res

    
    """
題目描述
給定一個二維矩陣 grid，其中每個元素要麼是 0 要麼是 1。你可以選擇任意數量的行或列進行翻轉，使得翻轉後的行的第一個元素都是 1。每行的分數是按二進位考量的，第一個元素是最高位。目標是透過翻轉，使矩陣的總分達到最大。

解題思路
確保每行的首位是 1：
首先，確保每行的第一個數字是 1，以最大化每行的數值。如果某行的第一個元素是 0，則翻轉整行。

優化每列：
從第二列開始，計算該列翻轉前後哪種情況更多的 1。如果翻轉後的 1 比翻轉前多，則執行翻轉。翻轉的目標是最大化每一列的 1 的數量，因為每個 1 都貢獻了該位的值。

計算總分：
根據每一列 1 的數量和它們各自的二進制價值計算總分。


時間複雜度和空間複雜度
時間複雜度：O(n*m)，其中 n 是行數，m 是列數。每個元素都會被訪問一次以決定翻轉策略。
空間複雜度：O(1)，僅使用了固定的額外空間
    """