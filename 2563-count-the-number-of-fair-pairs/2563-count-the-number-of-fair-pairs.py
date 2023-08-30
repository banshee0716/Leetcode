# 導入 List 類型標註
from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # 定義 countLess 函數
        def countLess(val: int) -> int:
            # 初始化 res 和 j
            res, j = 0, len(nums) - 1
            # 使用 for 迴圈遍歷數組
            for i in range(len(nums)):
                # 使用 while 迴圈減小 j 的值，使得 nums[i] + nums[j] 不超過 val
                while i < j and nums[i] + nums[j] > val:
                    j -= 1
                # 計算符合條件的對的數量，並累加到 res
                res += max(0, j-i)
            # 返回 res
            return res
        
        # 對 nums 進行排序
        nums.sort()
        # 計算並返回符合條件的對的數量
        return countLess(upper) - countLess(lower - 1)

                
                
                
                
                
                
                
                
                
        
        
        
        """
給定一個大小為 n 的 0 索引整數數組 nums 和兩個整數 lower 和 upper，返回公平對的數量。

一對 (i, j) 是公平（fair）的，如果：
    1. 0 <= i < j < n，並且
    2. 下限 <= nums[i] + nums[j] <= 上限
    
解題思路：
這題要求在給定的整數陣列 nums 中找出所有 "公平的" 數對 (i, j)，其中 nums[i] + nums[j] 要在 [lower, upper] 的範圍內。

這個問題可以透過排序和雙指針方法來解決。首先，對 nums 陣列進行排序。然後，定義一個函數 countLess(val) 來計算所有數對 (i, j) 的和小於等於 val 的數量。

最後，我們計算 countLess(upper) - countLess(lower - 1)，這樣就能得到所有和在 [lower, upper] 範圍內的數對的數量。

時間複雜度: 排序的時間複雜度是 O(n log n)，countLess 函數中的兩個迴圈的時間複雜度為 O(n)。所以總的時間複雜度是 O(n log n + n) = O(n log n)。
空間複雜度: 我們只用了常數的額外空間，所以空間複雜度是 O(1)。
        """