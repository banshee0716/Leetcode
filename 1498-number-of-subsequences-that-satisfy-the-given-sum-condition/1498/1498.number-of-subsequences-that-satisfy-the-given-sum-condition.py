#
# @lc app=leetcode id=1498 lang=python3
#
# [1498] Number of Subsequences That Satisfy the Given Sum Condition
#

# @lc code=start
"""
這個問題要求求給定數組nums中，所有和不超過target的子序列的個數。
我們可以使用雙指針的方法來解決這個問題。
首先對數組進行排序，然後遍歷每個元素，使用一個指針從當前元素的右邊開始向左移動，找到與當前元素和不超過target的位置。
在這個過程中，對於每個合法的子序列，我們可以計算出從當前位置到右指針之間的子序列個數，並累加到結果中。
"""
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()  # 對數組進行排序
        n = len(nums)
        res = 0
        mod = 10**9 + 7  # 模數，避免結果過大
        i, j = 0, n - 1  # 初始化雙指針，分別指向數組的開頭和結尾

        for i in range(n):  # 遍歷數組中的每個元素
            while i <= j and nums[i] + nums[j] > target:  # 如果當前和大於target，則將右指針向左移動
                j -= 1

            if i <= j and nums[i] + nums[j] <= target:  # 如果找到了和不超過target的子序列
                res += pow(2, (j - i), mod)  # 計算從當前位置到右指針之間的子序列個數，並累加到結果中
                res %= mod  # 對結果取模

        return res  # 返回最終結果

"""
時間複雜度：O(nlogn + n)，
其中n為數組的長度。排序的時間複雜度為O(nlogn)，遍歷數組的時間複雜度為O(n)。

空間複雜度：O(logn)，
其中n為數組的長度。主要是由於排序所需的空間，其他變數使用的空間為常數級別。
"""

# @lc code=end

