class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            # 如果找到目標值，直接返回其索引
            if nums[mid] == target:
                return mid
            # 若中點值小於目標值，有兩種可能
            elif nums[mid] < target:
                # 若開始點小於等於目標且開始點大於中點值
                # 這意味著左邊部分是有序的，且目標在左邊
                if nums[start] <= target and nums[start] > nums[mid]:
                    end = mid - 1
                # 否則，目標應在右邊
                else:
                    start = mid + 1
            # 若中點值大於目標值，有兩種可能
            elif nums[mid] > target:
                # 若目標小於等於結束點且結束點小於中點值
                # 這意味著右邊部分是有序的，且目標在右邊
                if target <= nums[end] and nums[end] < nums[mid]:
                    start = mid + 1
                # 否則，目標應在左邊
                else:
                    end = mid - 1

        # 若循環結束後仍未找到目標，返回-1
        return -1

        
"""

時間複雜度: O(logN)，其中 N 是 nums 的長度。即使數組是部分排序的，但我們仍使用二分搜索，因此時間複雜度為 O(logN)。

空間複雜度: O(1)。我們只使用了固定的額外空間。
"""