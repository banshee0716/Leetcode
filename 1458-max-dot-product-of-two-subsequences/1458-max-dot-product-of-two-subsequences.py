import math
from typing import List

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [-math.inf] * (m + 1)
        for i in range(1, n + 1):
            dp, old_dp = [-math.inf], dp  # old_dp 存放上一行的dp值
            for j in range(1, m + 1):
                # 更新dp[j]的值，考慮上述的四種選擇
                dp += max(
                    old_dp[j], # 不選 i
                    dp[-1], # 不選 j
                    old_dp[j - 1], # 都不選
                    max(old_dp[j - 1], 0) + nums1[i - 1] * nums2[j - 1], # 都選
                ),
        return dp[-1]

    """
    解題思路：

1. 使用一個動態規劃dp陣列來存儲結果，其中dp[j]表示考慮nums1的前i個元素和nums2的前j個元素時，最大的點積值。
2. 對於每一個位置(i, j)，我們有四種選擇：(1)不選nums1[i]；(2)不選nums2[j]；(3)都不選；(4)都選。
3. 對於每一種選擇，我們計算其對應的點積並更新dp[j]的值。

時間複雜度分析：
因為有兩個循環，分別是n和m，所以時間複雜度為O(n×m)。

空間複雜度分析：
我們只使用了固定大小的一維列表來存儲動態規劃的結果，所以空間O(m)。
    """