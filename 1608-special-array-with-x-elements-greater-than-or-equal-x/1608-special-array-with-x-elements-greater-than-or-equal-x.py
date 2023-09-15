class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # 降序排序 nums
        nums.sort(reverse=True)
        
        # 初始化二分搜索的左、右邊界
        left, right = 0, len(nums)
        
        while left < right:
            mid = left + (right - left) // 2  # 計算中間值
            
            # 如果 mid 小於 nums[mid]，意味著 nums 中至少有 mid+1 個數字大於或等於 mid
            # 因此我們將搜索範圍移動到 [mid+1, right]
            if mid < nums[mid]:
                left = mid + 1
            else:
                right = mid
        
        # 檢查結果是否有效
        return -1 if left < len(nums) and left == nums[left] else left
"""
找到一個特殊的數字x，使得nums中有恰好x個數大於或等於x。如果存在多個這樣的x，則返回最小的x。如果不存在這樣的x，則返回-1。

解題思路：
1. 首先，對nums進行降序排序。
2. 然後，使用二分搜索在範圍[0, len(nums)]中查找x，其中left和right分別表示搜索的範圍。
3. 在每次迭代中，我們計算mid作為可能的x。如果mid小於nums[mid]，則將搜索範圍縮小到[mid+1, right]，否則縮小到[left, mid]。
4. 最後，我們檢查找到的left是否是有效的x。

時間複雜度：O(n log n)，其中 n 是 nums 的大小。排序需要O(n log n)，二分搜索需要O(log n)。
空間複雜度：O(1)，因為我們只使用了常數的額外空間。
"""