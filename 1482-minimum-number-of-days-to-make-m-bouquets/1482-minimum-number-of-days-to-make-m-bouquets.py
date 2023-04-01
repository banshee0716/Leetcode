class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # 定義一個輔助函數來檢查在給定的天數內是否可以製作指定數量的花束
        def feasible(days) -> bool:
            # 初始化花束數量和已檢查的花朵數量
            bonquets, flowers = 0, 0
            # 遍歷每一朵花的開花時間
            for bloom in bloomDay:
                if bloom > days:  # 如果開花時間大於給定的天數，重新開始計算花朵數量
                    flowers = 0  
                else:
                    # 計算在這段時間內可以製作的花束數量和剩餘的花朵數量
                    bonquets += (flowers + 1) // k
                    flowers = (flowers + 1) % k
            # 檢查是否可以製作至少m個花束
            return bonquets >= m

        # 如果總花朵數量小於需要的花朵數量，則返回-1
        if len(bloomDay) < m * k:
            return -1

        left, right = 1, max(bloomDay)
        while left < right:
            mid = left + (right - left) // 2  
            if feasible(mid):  # 如果可以製作指定數量的花束
                right = mid  # 縮小右邊界
            else:
                left = mid + 1  # 縮小左邊界

        # 返回最小的天數
        return left
