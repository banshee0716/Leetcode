class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        # 首先，對數組進行排序。這使我們能夠快速計算任意兩個相鄰數字的差異。
        nums.sort()
        n = len(nums)

        # 初始化二分查找的範圍。左邊界是0，右邊界是數組中的最大差異。
        left, right = 0, nums[-1] - nums[0]

        # 進行二分查找
        while left < right:
            mid = left + (right - left) // 2

            # k是我們可以形成的對數。i是我們當前正在考慮的索引。
            k, i = 0, 1
            while i < n:
                # 如果當前差異小於或等於mid，則我們可以形成一對
                if nums[i] - nums[i-1] <= mid:
                    k += 1
                    i += 1
                # 移動到下一個索引
                i += 1

            # 如果我們可以形成的對數大於或等於p，則將右邊界設為mid
            if k >= p:
                right = mid
            # 否則，將左邊界設為mid+1
            else:
                left = mid + 1

        return left

        
        
    """
解題思路:

1. 對數組排序。
2. 使用二分查找找到滿足我們條件的最小的最大差異。給定一個可能的差異，我們計算可以形成的對數。
3. 根據形成的對數更新我們的查找範圍。


時間複雜度:
排序：O(nlogn)
二分查找：O(nlog(max_difference))
總的時間複雜度為：O(nlogn)

空間複雜度:
此方法的空間複雜度為O(1)，因為我們只使用了常數的額外空間。
    """