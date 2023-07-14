class Solution:
    def longestSubsequence(self, nums, difference):
        # 初始化一個空字典來保存以某個數字結尾的最長等差子序列的長度
        dp = {}
        # 初始化最長等差子序列的長度為1
        max_length = 1

        # 遍歷輸入的數組
        for num in nums:
            # 檢查當前數字的前一個等差數字是否在dp中
            if num - difference in dp:
                # 如果存在，則當前數字可以擴展前一個數字的等差子序列
                dp[num] = dp[num - difference] + 1
            else:
                # 否則，當前數字開始一個新的等差子序列
                dp[num] = 1

            # 更新最長等差子序列的長度
            max_length = max(max_length, dp[num])

        # 返回最長等差子序列的長度
        return max_length

"""
1. 我們遍歷輸入的數組nums。

2. 對於每一個數字，我們查看其前一個等差數字（即num - difference）在dp中是否存在。如果存在，我們就知道我們可以在這個等差子序列後面再加上這個數字，所以dp[num]應該是dp[num - difference] + 1。如果不存在，這個數字就會開始一個新的等差子序列。

3. 我們同時記錄下最長的等差子序列的長度。


時間複雜度是O(N)，其中N是數組nums的長度，因為我們需要遍歷一次數組。
空間複雜度是O(M)，其中M是數組中出現的不同數字的數量，這就是字典dp需要使用的空間大小。
"""