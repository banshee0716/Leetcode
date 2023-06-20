class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        L = len(nums)  # 獲取 nums 的長度
        res = [-1] * L  # 初始化結果陣列

        i = k  # 從索引 k 開始計算平均值

        # 初始的窗口大小為 2k+1，求和
        s = sum(nums[: k * 2 + 1])
        a = k * 2 + 1  # 平均值的分母，也就是窗口大小

        # 從索引 k 開始，向右滑動窗口，直到窗口右邊界達到陣列終點
        while i < L - k:
            res[i] = int(s / a)  # 計算並儲存窗口內的平均值
            i += 1  # 窗口向右移動
            if i < L - k:
                # 滑動窗口，加上新進入窗口的值，減去離開窗口的值
                s = s + nums[i + k] - nums[i - k - 1]

        return res  # 返回結果陣列
"""
時間複雜度是 O(n)，其中 n 是陣列 nums 的長度。我們只需遍歷一次這個陣列。
空間複雜度是 O(n)，其中 n 是陣列 nums 的長度。我們創建了一個與 nums 相同大小的結果陣列來儲存結果。
"""