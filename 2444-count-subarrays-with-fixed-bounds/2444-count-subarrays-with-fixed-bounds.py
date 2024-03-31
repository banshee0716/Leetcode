from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        bad_index = left_index = right_index = -1
        res = 0
        
        for i, num in enumerate(nums):
            # 如果當前數不在[minK, maxK]範圍內，更新bad_index
            if not minK <= num <= maxK:
                bad_index = i
                
            # 如果當前數等於minK，更新left_index
            if num == minK:
                left_index = i
            
            # 如果當前數等於maxK，更新right_index
            if num == maxK:
                right_index = i
            
            # 計算有效的固定界限子數組數量
            res += max(0, min(left_index, right_index) - bad_index)
            
        return res

    
    
    """
給定一個整數數組nums和兩個整數minK與maxK，固定界限子數組是指滿足以下條件的子數組：

    -子數組中的最小值等於minK。
    -子數組中的最大值等於maxK。

題目要求返回固定界限子數組的數量。

解題思路
此問題可以透過維護三個指針來解決：

1. bad_index：指向最近一個不在[minK, maxK]區間內的元素的索引。
2. left_index：從左至右，指向最近一個等於minK的元素的索引。
3. right_index：從左至右，指向最近一個等於maxK的元素的索引。
    
時間複雜度分析
此算法只需要遍歷一次數組nums，因此時間複雜度為O(N)，其中N是數組nums的長度。

空間複雜度分析
此算法除了給定的輸入數組外，只使用了固定的額外空間來存儲幾個索引和結果變量，因此空間複雜度為O(1)。
    """