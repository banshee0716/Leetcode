import random

class Solution:
    def findKthLargest(self, nums, k):
        def quick_select(nums, k):
            # 隨機選取一個基準值(pivot)
            pivot = random.choice(nums)
            left, mid, right = [], [], []
            
            # 根據基準值將nums中的數字劃分成三部分
            # left: 大於基準值的數字
            # mid: 等於基準值的數字
            # right: 小於基準值的數字
            for num in nums:
                if num > pivot:
                    left.append(num)
                elif num < pivot:
                    right.append(num)
                else:
                    mid.append(num)

            # 如果k小於等於left的長度，那麼答案在left中
            if k <= len(left):
                return quick_select(left, k)
            
            # 如果k大於left的長度加上mid的長度，那麼答案在right中
            if len(left) + len(mid) < k:
                return quick_select(right, k - len(left) - len(mid))
            
            # 否則，答案就是基準值
            return pivot
        
        return quick_select(nums, k)

"""
一個裸的quick select
解題思路：

隨機選擇一個數字作為基準值。
根據基準值將nums劃分成三部分：大於基準值的數字、等於基準值的數字和小於基準值的數字。
判斷k所在的區間，並在該區間進行遞迴搜尋。
時間複雜度：平均情況下為O(n)，最壞情況下為O(n^2)，其中n是nums的長度。但由於我們使用了隨機選擇基準值的策略，所以大多數情況下的效能都很好。

空間複雜度：O(1)，除非考慮遞迴調用棧的大小，那麼最壞情況下為O(n)。
"""