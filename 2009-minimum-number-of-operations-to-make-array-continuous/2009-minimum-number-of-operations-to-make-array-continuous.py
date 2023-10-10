from typing import List
from bisect import bisect_right

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        # 先將數組去重並排序
        nums = sorted(set(nums))
        
        ans = n
        for i, start in enumerate(nums):
            # 計算預期的連續整數範圍的結尾
            end = start + n - 1
            
            # 使用二分法找到右插入位置
            idx = bisect_right(nums, end)
            
            # 計算此範圍內有多少唯一整數
            uniqueLen = idx - i
            
            # 更新答案
            ans = min(ans, n - uniqueLen)
            
        return ans

        
    """

解題思路是:

1. 首先，將數組去重並排序。
2. 然後，遍歷每一個數字，試圖找到一個連續的整數範圍，使得該範圍內已經存在的整數最多。

時間複雜度分析：
1. 對 nums 去重和排序，時間複雜度是 O(nlogn)。
2. 遍歷整個數組，並在其中使用 bisect_right 函數，時間複雜度還是 O(nlogn)。
總時間複雜度是 O(nlogn)。

空間複雜度分析：
我們使用了一個額外的已排序陣列 nums，空間複雜度是 O(n)。
    """