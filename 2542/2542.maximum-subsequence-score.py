#
# @lc app=leetcode id=2542 lang=python3
#
# [2542] Maximum Subsequence Score
#


# @lc code=start
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        total = res = 0  # 初始的總和和最終結果都設為0
        heap = []  # 創建一個空的heap

        pairs = zip(nums1, nums2)  # 將兩個列表組合成數對

        # 依據每個數對的第二個數字進行排序，由大到小
        sorted_pairs = sorted(pairs, key=lambda x: -x[1])

        for pair in sorted_pairs:
            num1, num2 = pair  # 解析數對
            heappush(heap, num1)  # 將數對的第一個數字加入heap
            total += num1  # 累計數對的第一個數字的總和
            if len(heap) > k:  # 如果heap的長度超過k
                total -= heappop(heap)  # 則移除heap中最小的數字，並從總和中減去
            if len(heap) == k:  # 如果heap的長度等於k
                res = max(res, total * num2)  # 更新最終結果

        return res  # 返回最終結果


# @lc code=end
