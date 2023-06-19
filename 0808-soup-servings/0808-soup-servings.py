class Solution:
    memo = {}  # 建立一個字典來儲存已經計算過的情況
    
    def soupServings(self, N: int) -> float:
        if N > 4800: return 1  # 如果 N 大於 4800，直接返回 1
        def f(a, b):
            if (a, b) in self.memo:  # 如果 (a, b) 已經計算過，直接從字典中取出
                return self.memo[a, b]
            if a <= 0 and b <= 0: return 0.5  # 如果 a 和 b 都小於等於 0，返回 0.5
            if a <= 0: return 1  # 如果 a 小於等於 0，返回 1
            if b <= 0: return 0  # 如果 b 小於等於 0，返回 0
            # 計算當前情況下的機率
            self.memo[(a, b)] = 0.25 * (f(a - 4, b) + f(a - 3, b - 1) + f(a - 2, b - 2) + f(a - 1, b - 3))
            return self.memo[(a, b)]  # 返回計算結果
        N = math.ceil(N / 25.0)  # 將 N 除以 25 並向上取整
        return f(N, N)  # 計算並返回結果
"""
首先如果給定的 N 大於 4800，根據題目的描述，我們可以直接返回 1。
接著我們定義函數 f(a, b)，它代表當前湯 A 有 a 毫升，湯 B 有 b 毫升時，最終湯 A 先空的機率。

時間複雜度是 O(N^2)，因為我們需要遍歷所有可能的 (a, b)。
空間複雜度也是 O(N^2)，因為我們需要儲存所有可能的 (a, b) 的結果。其中 N 是原始的湯的量。
"""