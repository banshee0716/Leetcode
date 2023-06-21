class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        # 定義一個輔助函數 f(x)，計算以 x 為目標值時，總成本
        def f(x):
            return sum(abs(a - x) * c for a, c in zip(nums, cost))

        # 初始化範圍為 nums 中最小和最大的值
        l, r = min(nums), max(nums)

        # 預先計算一個初始成本值
        res = f(l)

        # 使用二分搜索找到最小的成本
        while l < r:
            # 將範圍一分為二
            x = (l + r) // 2

            # 計算兩個點的成本
            y1, y2 = f(x), f(x + 1)

            # 更新最小成本
            res = min(y1, y2)

            # 根據兩個點的成本決定下一步的搜索範圍
            if y1 < y2:
                r = x
            else:
                l = x + 1

        return res  # 返回最小成本


"""
時間複雜度為 O(n log n)，其中 n 是陣列 nums 的長度。我們在每次迭代中計算兩個成本值，每次成本計算需要遍歷 nums，且迭代次數與 nums 範圍的大小有關，進行了 log n 次迭代。

空間複雜度為 O(1)。我們僅創建了數個輔助變數，而且沒有與輸入大小相關的額外數據結構。

"""
