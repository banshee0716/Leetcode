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

1. 該代碼遍歷nums列表，對於每個數字num，它檢查dp字典中是否存在前一個數字num - difference。如果存在num - difference，這意味著存在以num - difference結尾的子序列。

2. 在這種情況下，代碼通過將num包含在末尾來擴展子序列。它將dp[num]賦值為dp[num - difference] + 1，表示以num結尾的子序列的長度比以num - difference結尾的子序列長度多1。

3.如果dp字典中不存在num - difference，則意味著不存在以num - difference結尾的先前子序列。在這種情況下，代碼將dp[num]初始化為1，表示該子序列只包含num。

4.在遍歷過程中，代碼還跟踪迄今為止找到的最大長度。它使用max函數更新max_length，將以num結尾的子序列長度與當前最大長度進行比較。

5. 在遍歷nums列表中的所有數字之後，代碼返回最大長度，該最大長度表示具有給定差值的最長等差子序列的長度。


時間複雜度是O(N)，其中N是數組nums的長度，因為我們需要遍歷一次數組。
空間複雜度是O(M)，其中M是數組中出現的不同數字的數量，這就是字典dp需要使用的空間大小。
"""