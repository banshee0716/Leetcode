from typing import List

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        # 初始化計數數組，範圍為0到n
        counts = [0] * (n + 1)

        # 統計每個元素出現的次數
        for num in arr:
            counts[min(num, n)] += 1

        ans = 1
        # 遍歷並重建數組，確保相鄰元素差值不超過1
        for num in range(2, n + 1):
            ans = min(ans + counts[num], num)

        return ans

# 使用black格式化後的代碼與上述代碼在格式上已經符合標準
"""
計數排序：
1. 首先，使用一個數組 counts 來統計每個元素出現的次數。由於數組的長度為 n，任何大於 n 的元素都可以被減少到 n 或更小，因此只需考慮 0 到 n 的範圍。

2. 然後，從 1 開始遍歷 counts 數組，每次嘗試將當前數字 num 的值增加 counts[num]（即出現的次數），但不超過 num 本身。這是因為，為了保持相鄰元素差值不超過 1，當前元素的最大值應該不超過前一個元素的值加 1。

最終，ans 中存儲的是經過重建後的數組可能的最大元素。


時間複雜度分析：
遍歷數組 arr 並統計元素出現次數的時間複雜度為 O(n)，其中 n 為數組長度。
遍歷 counts 數組的時間複雜度同樣為 O(n)。

空間複雜度分析：
除了原始數組外，額外使用了一個長度為 n+1 的 counts 數組，因此空間複雜度為 O(n)。
"""