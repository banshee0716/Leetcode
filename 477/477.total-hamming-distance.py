#
# @lc app=leetcode id=477 lang=python3
#
# [477] Total Hamming Distance
#

# @lc code=start
""" 

這裡的程式碼使用了位操作的技巧。解題思路是，我們對於每個位，統計有多少個數字在該位為 1，這樣就可以知道在該位的漢明距離的總和。例如，如果有 k 個數字在某位為 1，則在該位的漢明距離總和為 k * (n - k)。
"""
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)  # 數字的總數
        result = 0  # 總漢明距離
        for i in range(30):  # 遍歷每一位，因為整數範圍在 0 到 10^9，所以最多需要考慮30位
            count = 0  # 記錄該位為 1 的數字的數量
            for num in nums:  
                count += (num >> i) & 1  # 如果該位為 1，則 count 加 1
            result += count * (n - count)  # 累加該位的漢明距離
        return result  # 返回總漢明距離

# @lc code=end

