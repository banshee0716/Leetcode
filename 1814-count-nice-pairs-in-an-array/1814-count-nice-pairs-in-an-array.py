from typing import List

class Solution:
    def reverse(self, num: int) -> int:
        # 反轉一個數字
        rev = 0
        while num > 0:
            rev = rev * 10 + num % 10
            num //= 10
        return rev

    def countNicePairs(self, nums: List[int]) -> int:
        mod = 1000000007

        # 變換數組
        nums = [num - self.reverse(num) for num in nums]

        # 排序變換後的數組
        nums.sort()

        res = 0
        i = 0
        # 遍歷數組計算每個唯一數字的出現次數
        while i < len(nums) - 1:
            cont = 1
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                cont += 1
                i += 1
            # 計算可愛對的數量
            res = (res % mod + (cont * (cont - 1)) // 2) % mod
            i += 1

        return int(res % mod)

# 使用black格式化後的代碼與上述代碼在格式上已經符合標準
"""
解題思路：

計算差值：
遍歷數組中的每個數字，計算 num - rev(num) 的差值，這個操作會將原問題轉化為查找數組中相同數字的對數。

排序和計數：
排序變換後的數組，這樣相同的數字會排列在一起，便於計數。
使用雙重循環來計算數組中每個唯一數字的出現次數，並根據組合數公式計算可愛對的數量。

計算結果：
最後，計算並返回所有可愛對的總數。

時間複雜度分析：
反轉數字的時間複雜度是 O(log n)，其中 n 是數字的大小。
變換數組的時間複雜度是 O(N log M)，其中 N 是數組長度，M 是數組中數字的最大值。
排序的時間複雜度是 O(N log N)。
遍歷並計數的時間複雜度是 O(N)。
總的時間複雜度是 O(N log N + N log M)。

空間複雜度分析：
需要額外的空間來存儲變換後的數組，所以空間複雜度是 O(N)。
"""