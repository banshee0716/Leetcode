from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # 初始化 dp，大小為 target + 1
        dp = [0] * (target + 1)
        
        # 當目標是0時，有一種組合方法
        dp[0] = 1
        
        # 遍歷1到target
        for i in range(target+1):
            # 遍歷 nums 中的每一個數字
            for num in nums:
                # 如果 num 可以被用來組成 i
                if num <= i:
                    # 更新 dp[i]
                    dp[i] += dp[i-num]
        
        # 返回最後一個值，即 dp[target]
        return dp[-1]

"""
解題思路：
1. 動態規劃：我們使用動態規劃的方法來解這題，其中 dp[i] 表示組成整數 i 的組合數。
2. 初始化：dp[0] = 1，因為數組中沒有元素時，只有一種組合（即空組合）可以組成目標值 0。
3. 狀態轉移：對於每一個 i（1 到 target），我們遍歷 nums 中的每一個數字 num。如果 num 小於或等於 i，則 dp[i] += dp[i-num]，意味著我們可以用 num 來組成 i。

時間複雜度：我們遍歷了 1 到 target，每次遍歷時都要遍歷 nums 中的所有元素，所以時間複雜度是 O(n×m)，其中n 是 target 的大小，m 是 nums 的大小。

空間複雜度：我們使用了一個大小為 target + 1 的 dp 陣列，所以空間複雜度是 O(n)。
"""