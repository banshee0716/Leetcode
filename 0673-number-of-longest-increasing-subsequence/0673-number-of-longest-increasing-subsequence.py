class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        
        n = len(nums)
        dp, cnt = [1] * n, [1] * n  # dp[i]: 長度, cnt[i]: 數量
        m = 0  # 最長子序列的長度

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] < dp[j] + 1:
                        dp[i], cnt[i] = dp[j] + 1, cnt[j]
                    elif dp[i] == dp[j] + 1:
                        cnt[i] += cnt[j]
            m = max(m, dp[i])

        return sum(c for l, c in zip(dp, cnt) if l == m)

"""

1. 首先，如果列表是空的，則返回0，因為沒有任何子序列。

2. 初始化兩個列表，dp 和 cnt，都是長度為n（n是列表nums的長度）的列表，其中dp[i]表示在nums[0...i]的範圍內最長遞增子序列的長度，cnt[i]表示在nums[0...i]的範圍內最長遞增子序列的數量。

3. 遍歷列表中的每一個元素，對於每一個元素nums[i]，遍歷其之前的所有元素nums[j]，如果nums[j] < nums[i]，則有可能形成一個新的遞增子序列或者延長已經存在的遞增子序列。
    - 如果 dp[j]+1 > dp[i]，表示找到了一個更長的遞增子序列，更新dp[i]為dp[j]+1，同時，這種遞增子序列的數量應該與dp[j]相同，所以更新cnt[i]為cnt[j]。
    - 如果 dp[j]+1 == dp[i]，表示找到了一個與當前最長遞增子序列相同長度的新遞增子序列，所以應該將這些新遞增子序列的數量加到cnt[i]上，所以更新cnt[i]為cnt[i] + cnt[j]。

4. 最後，找出dp中的最大值，然後返回cnt中與這個最大值對應的總數。

時間複雜度是O(n^2)，因為我們對列表中的每一個元素，都需要遍歷其之前的所有元素。
空間複雜度是O(n)，因為我們需要兩個長度為n的列表來儲存每個位置的狀態。
"""