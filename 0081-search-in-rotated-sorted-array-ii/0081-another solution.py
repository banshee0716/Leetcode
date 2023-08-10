class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (r + l) // 2

            # 若目標值等於中點、左邊界或右邊界的值，則返回True
            if target in [nums[m], nums[r], nums[l]]:
                return True

            # 若中點值等於左邊界或右邊界的值，則兩邊都收縮1
            elif nums[m] == nums[l] or nums[m] == nums[r]:
                r -= 1
                l += 1

            # 若左邊界的值小於等於中點值，則左半部分是有序的
            elif nums[l] <= nums[m]:
                # 若目標在左邊界和中點之間，則在左半部分搜索
                if nums[l] < target < nums[m]:
                    r = m - 1
                # 否則，在右半部分搜索
                else:
                    l = m + 1

            # 若左邊界的值大於中點值，則右半部分是有序的
            else:
                # 若目標在中點和右邊界之間，則在右半部分搜索
                if nums[m] < target < nums[r]:
                    l = m + 1
                # 否則，在左半部分搜索
                else:
                    r = m - 1

        # 若搜索結束後沒有找到目標值，則返回False
        return False

        """
        解題思路:

初始化左邊界和右邊界。
比較中點、左邊界和右邊界的值，以判斷要在哪一半進行搜索。
根據上述比較的結果，更新左邊界或右邊界。
時間複雜度:
在最壞的情況下，可能需要考慮到陣列中的每一個元素，因此時間複雜度為O(n)。但在平均情況下，仍然是二分查找的特性，因此時間複雜度接近O(log n)。

空間複雜度:
此方法的空間複雜度為O(1)，因為我們只使用了常數的額外空間。
        """
