class Solution:
    def check(self, a):
        left_offset = max(a - self.index, 0)
        # 這裡計算左半部分數列的和，使用等差數列的求和公式
        result = (a + left_offset) * (a - left_offset + 1) // 2
        right_offset = max(a - ((self.n - 1) - self.index), 0)
        # 這裡計算右半部分數列的和，使用等差數列的求和公式
        result += (a + right_offset) * (a - right_offset + 1) // 2
        return result - a

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        self.n = n
        self.index = index

        maxSum -= n  # 減去每個數組元素最小的值
        left, right = 0, maxSum  # 二分搜尋的左右邊界
        while left < right:  # 進行二分搜尋
            mid = (left + right + 1) // 2  # 計算中間值
            if self.check(mid) <= maxSum:  # 如果中間值的和小於等於maxSum，則移動左邊界
                left = mid
            else:  # 否則移動右邊界
                right = mid - 1
        result = left + 1  # 最後找到的左邊界就是需要的最大值
        return result
"""
解題思路:

首先，減去每個數組元素最小的值，使問題簡化為找出一個數組，該數組中每個元素都大於等於1，且其總和不超過maxSum。然後，使用二分搜尋法找出該數組中的最大值。

時間複雜度:

O(log(maxSum)) - 進行二分查找，所以時間複雜度為O(log(maxSum))。
空間複雜度:

O(1) - 這個演算法只使用了常數的額外空間。

"""