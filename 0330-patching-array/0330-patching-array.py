from typing import List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        reach, ans, idx = 0, 0, 0  # 初始化覆蓋範圍、答案和索引

        while reach < n:
            # 利用現有數組元素擴大覆蓋範圍
            if idx < len(nums) and nums[idx] <= reach + 1:
                reach += nums[idx]
                idx += 1
            else:
                # 需要添加數字來擴大覆蓋範圍
                ans += 1
                reach = reach * 2 + 1

        return ans

        
        
        
    """
    
解題思路：

1. 貪心算法：
    -使用貪心算法來解決這個問題。維護一個變量 reach，表示目前能夠覆蓋到的最大數字。

2. 檢查和更新 reach：
    -遍歷數組 nums。如果當前數組元素 nums[idx] 小於或等於 reach + 1，則更新 reach 為 reach + nums[idx]，表示利用現有的數組元素能覆蓋更大範圍的數字。
    -如果 nums[idx] 大於 reach + 1，則需要添加一個新數字。這個新數字應該是 reach + 1，因為這是當前無法覆蓋的最小數字。添加這個數字後，更新 reach 為 reach * 2 + 1。

3.返回結果：
    -當 reach 大於或等於 n 時，停止遍歷，返回添加的數字數量 ans。

時間複雜度分析：
在最壞的情況下，算法會遍歷整個數組 nums 並添加一些數字。遍歷和添加操作的時間複雜度都是 O(log n)，因為每次添加數字後，覆蓋範圍至少翻倍。
總的時間複雜度為 O(log n)。

空間複雜度分析：
這個算法只使用了固定的額外空間來存儲變數，因此空間複雜度為 O(1)。
    """