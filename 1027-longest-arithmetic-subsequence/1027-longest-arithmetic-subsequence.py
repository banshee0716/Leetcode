class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}  # dp[i, d]代表以第i個數字為結尾，並且等差為d的最長等差序列長度
        for i, a2 in enumerate(nums[1:], start=1):  # 從第二個數字開始遍歷，a2代表當前的數字
            for j, a1 in enumerate(nums[:i]):  # 遍歷a2前面的所有數字，a1代表前面的數字
                d = a2 - a1  # 計算等差
                # 如果在dp中已經存在以a1為結尾，並且等差為d的序列，則在該序列長度上加1
                if (j, d) in dp:
                    dp[i, d] = dp[j, d] + 1
                # 否則，創建一個新的序列，長度為2
                else:
                    dp[i, d] = 2
        # 返回最長的等差序列長度
        return max(dp.values()) 

"""
使用動態規劃的方法。
動態規劃的基本思想是將一個複雜的問題分解為較小的子問題，並存儲已解決的子問題的結果，進行重複利用。這題中的子問題是：以第i個數字為結尾，並且等差為d的最長等差序列長度是多少


時間複雜度為 O(n^2)，其中 n 是輸入序列的長度。因為我們需要對每對數字(a1, a2)計算等差並更新dp。
空間複雜度為 O(n^2)，在最壞情況下，每一對數字(a1, a2)的等差都不同，我們需要存儲所有的dp[i, d]。
"""