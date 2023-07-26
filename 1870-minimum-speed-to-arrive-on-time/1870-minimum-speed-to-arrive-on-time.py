class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        # 為二分搜尋定義初始的左邊界和右邊界
        left, right, n = 1, 10**7 + 1, len(dist)

        # 二分搜尋
        while left < right:
            # 計算當前範圍的中點
            speed = left + (right - left) // 2

            # 計算以當前速度所需要的時間
            need = dist[-1] / speed + sum(
                (dist[i] + speed - 1) // speed for i in range(n - 1)
            )

            # 如果所需時間大於給定的時間，
            # 則將左邊界移到中點的右邊
            if need > hour:
                left = speed + 1
            # 如果所需時間小於或等於給定的時間，
            # 則將右邊界移到中點
            else:
                right = speed

        # 返回所需的最小速度，即左邊界
        return -1 if left == 10**7 + 1 else left


"""
1. 用了二分搜尋來尋找符合問題限制的最小速度。
2. 該解決方案首先初始化可能的速度範圍為 [1, 10**7 + 1]。變數n是dist的長度，代表了段數。然後在這個速度範圍內進行二分搜尋。
3. while迴圈是二分搜尋的實現。對於每一次迭代，它計算當前範圍 [left, right) 的中點speed，並計算以這個速度到達目的地所需要的時間need。
4. 如果需要的時間need超過了給定的hour，則將左邊界更新為speed + 1，否則，將右邊界更新為speed。這個過程繼續進行，直到左邊界等於右邊界。
5. 最後，函數返回左邊界作為所需的最小速度。

時間複雜度，它是O(n log m)，其中n是dist的長度，m是可能的最大速度（在這個案例中為10**7），因為二分搜尋是在速度範圍上進行，並且對於每一種速度，我們都遍歷dist來計算所需時間。

空間複雜度為O(1)，因為我們只使用了一定量的空間來存儲變數left、right、n、speed和need。
"""
