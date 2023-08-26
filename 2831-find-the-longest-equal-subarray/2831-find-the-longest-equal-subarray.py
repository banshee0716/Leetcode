from typing import List
from collections import defaultdict


class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0  # 初始化左指針
        hm = defaultdict(int)  # 初始化哈希表
        max_cnt = 0  # 初始化 max_cnt

        # 遍歷整個數組
        for right in range(n):
            # 更新哈希表
            hm[nums[right]] += 1
            # 更新 max_cnt
            max_cnt = max(max_cnt, hm[nums[right]])

            # 檢查是否需要縮小窗口
            if max_cnt + k < right - left + 1:
                # 更新哈希表和左指針
                hm[nums[left]] -= 1
                left += 1

        # 最後的結果會是窗口的大小
        return max_cnt


"""
解題思路
1. 使用滑動窗口的策略來解決這個問題。
2. 利用一個哈希表hm來記錄目前窗口中每個元素出現的次數。
3. 利用一個變量max_cnt來記錄目前窗口中出現次數最多的元素的出現次數。
4. 在擴大窗口（也就是right指針向右移動）的過程中，不斷更新max_cnt。
5. 如果窗口的大小超過max_cnt + k，則需要縮小窗口（也就是left指針向右移動）。

時間複雜度：
O(n)，其中n是數組nums的長度。因為我們只遍歷了數組一次。
空間複雜度：
O(u)，其中u是數組nums中唯一元素的數量。這是因為我們使用了一個哈希表來存儲每個元素的出現次數。
"""
