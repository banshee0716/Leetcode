class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        left, right, product, count = 0, 0, 1, 0
        
        while right < len(nums):
            product *= nums[right]
            while product >= k:
                product //= nums[left]
                left += 1
            
            count += 1 + (right-left)
            right += 1
        
        return count
            
        
        
"""
給定一個整數數組 nums 和一個整數 k，傳回連續子數組的數量，其中子數組中所有元素的乘積嚴格小於 k。

解題思路
這道題可以使用雙指針技巧來高效解決。具體方法是維護一個滑動窗口，窗口的乘積小於k，並動態調整窗口的大小。

1. 邊界條件處理：如果k <= 1，直接返回0，因為乘積不可能小於1（考慮到數組元素和k都是正整數）。
2. 初始化：初始化兩個指針left和right指向數組開頭，product記錄當前窗口內數字的乘積，count記錄符合條件的子數組數量。
3. 遍歷數組：遍歷數組，不斷將right指向的數字納入當前窗口的乘積中。
4. 調整窗口大小：當當前窗口內的乘積達到或超過k時，從窗口的左側排除數字，即將left指向的數字從product中移除，並將left右移。
5. 計算符合條件的子數組數量：每當窗口的乘積小於k時，窗口內從left到right的所有子數組都將符合條件。這些子數組的數量為right - left + 1。

時間複雜度分析
    -遍歷整個數組的時間複雜度為O(N)，其中N是數組nums的長度。
    -每個元素最多被product乘一次和除一次，因此總的時間複雜度仍為O(N)。

空間複雜度分析
    -本解法只使用了固定的額外空間（用於存儲指針、乘積和計數器等變量），因此空間複雜度為O(1)。
"""
        