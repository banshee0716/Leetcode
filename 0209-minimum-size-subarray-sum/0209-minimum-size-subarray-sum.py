class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 初始化左右指標和窗口內數字的總和
        left, right, total = 0, 0, 0
        # 初始化最小長度為數組長度加1（初始為一個無效值）
        min_len = len(nums) + 1

        # 遍歷整個數組
        while right < len(nums):
            # 將當前數字加入總和
            total += nums[right]
            # 向右移動right指標（擴大窗口）
            right += 1

            # 如果當前窗口的總和大於等於目標值
            while total >= target:
                # 更新最小長度
                min_len = min(min_len, right - left)
                # 從總和中減去left指標指向的數字，並將left指標向右移（收縮窗口）
                total -= nums[left]
                left += 1

        # 如果最小長度仍然是初始值，表示沒有找到符合條件的子數組
        if min_len == len(nums) + 1:
            return 0
        else:
            # 否則返回找到的最小長度
            return min_len

"""
時間複雜度為 O(n)，其中 n 是數組的長度。這是因為每個元素最多被訪問兩次，一次是由右指標訪問，一次是由左指標訪問。

空間複雜度為 O(1)，因為只使用了固定的額外空間。"""