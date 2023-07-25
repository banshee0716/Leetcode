class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        # 計算每一行中最小數字的和
        possible_min = sum(min(row) for row in mat)
        # 如果這個和比目標數字大，那麼直接返回兩者之間的差
        if possible_min > target:
            return possible_min - target

        # 初始化一個集合來儲存可能的和
        nums = {0}
        # 對於每一行的數字，更新可能的和的集合
        for row in mat:
            nums = {x + i for x in row for i in nums if x + i <= 2 * target - possible_min}

        # 返回與目標數字最接近的和的差的絕對值
        return min(abs(target - x) for x in nums)

"""

首先計算了所有行中最小的數字和作為可能的最小和，如果這個和比目標數字大，那麼直接返回兩者之間的差，因為任何選取的和都不可能比這個數字小。
接著，透過動態規劃的方式，計算出所有可能的和，並將它們儲存在一個集合中。最後，返回與目標數字最接近的和的差的絕對值。

考慮到我們需要環顧目標，我們可以優化解決方案。也就是說，如果所有數字的最小總和大於目標，我們別無選擇：我們需要接受它。在相反的情況下，不需要高於 2*target - possible_min

時間複雜度是 O(target * n^2)，空間複雜度是 O(target)。
"""