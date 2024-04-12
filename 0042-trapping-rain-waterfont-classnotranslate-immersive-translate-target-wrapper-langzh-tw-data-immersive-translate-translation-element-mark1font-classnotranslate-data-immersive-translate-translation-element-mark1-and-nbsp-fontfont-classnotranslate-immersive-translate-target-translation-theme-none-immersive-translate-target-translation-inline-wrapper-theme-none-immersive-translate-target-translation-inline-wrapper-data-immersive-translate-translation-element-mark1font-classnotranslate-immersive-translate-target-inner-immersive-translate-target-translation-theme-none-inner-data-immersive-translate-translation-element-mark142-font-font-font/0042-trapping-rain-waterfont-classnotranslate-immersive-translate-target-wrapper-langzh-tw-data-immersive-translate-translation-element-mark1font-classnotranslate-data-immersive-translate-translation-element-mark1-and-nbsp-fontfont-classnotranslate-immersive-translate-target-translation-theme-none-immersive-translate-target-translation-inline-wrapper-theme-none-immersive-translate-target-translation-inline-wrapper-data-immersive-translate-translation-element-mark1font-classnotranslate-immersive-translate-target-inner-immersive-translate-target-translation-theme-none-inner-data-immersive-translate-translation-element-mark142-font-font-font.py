from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        left_max, right_max = height[i], height[j]
        sumRain = 0
        
        while i < j:
            if left_max <= right_max:
                sumRain += left_max - height[i]  # 計算當前位置的雨水
                i += 1
                left_max = max(left_max, height[i])  # 更新左側最大值
            else:
                sumRain += right_max - height[j]  # 計算當前位置的雨水
                j -= 1
                right_max = max(right_max, height[j])  # 更新右側最大值
        
        return sumRain

    
    """
解題思路
此問題的核心是計算每個位置上能接多少雨水，這取決於左右兩側最高的障礙物。使用兩個指針i和j分別從數組的左右兩側開始向中心移動，並記錄兩側的最高高度left_max和right_max。

如果left_max小於或等於right_max，則i位置上能接的雨水由left_max決定。更新i處的最大值並向內移動。
如果right_max小於left_max，則j位置上能接的雨水由right_max決定。更新j處的最大值並向內移動。


時間複雜度分析
此方法只遍歷一次給定的高度數組，因此時間複雜度為O(N)，其中N是數組height的長度。

空間複雜度分析
這個算法只使用了固定數量的額外空間（用於存儲左右最大值和雙指針），因此空間複雜度為O(1)。
    """