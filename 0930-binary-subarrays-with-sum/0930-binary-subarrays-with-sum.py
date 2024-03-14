from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = {0: 1}  # 前綴和為0的情況初始為1次
        curr_sum = 0
        total_subarrays = 0
        
        for num in nums:
            curr_sum += num  # 計算當前前綴和
            # 如果curr_sum - goal在哈希表中，累加對應的子數組數量
            if curr_sum - goal in count:
                total_subarrays += count[curr_sum - goal]
            # 更新當前前綴和的計數
            count[curr_sum] = count.get(curr_sum, 0) + 1
            
        return total_subarrays

    
    
"""
解題思路
此題可以使用「前綴和」和「哈希表」來高效解決。基本思路是計算數組的前綴和，並在遍歷過程中使用一個哈希表記錄各個前綴和出現的次數。

初始化哈希表：
    －哈希表count用於記錄前綴和出現的次數。初始時，前綴和為0的情況出現了1次。

遍歷數組計算前綴和：
    －遍歷數組nums，計算當前的前綴和curr_sum。

查找並計數符合條件的子數組：
    －對於每個curr_sum，檢查curr_sum - goal是否在count哈希表中。如果存在，則count[curr_sum - goal]的值即為以當前元素結尾、和為goal的子數組的數量。
    －更新total_subarrays，累加找到的子數組數量。

更新哈希表：
    －在哈希表中更新當前前綴和curr_sum的計數。
    
時間複雜度
－遍歷數組的時間複雜度為O(N)，其中N是數組nums的長度。

空間複雜度
－哈希表count的空間複雜度最壞情況下為O(N)，因此總的空間複雜度也是O(N)。
"""