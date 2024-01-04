from collections import Counter
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        mp = Counter(nums)
        count = 0
        for t in mp.values():
            if t == 1:
                return -1
            count += t // 3
            if t % 3:
                count += 1
                
        return count
            
    
    
    """
給定一個由正整數組成的 0 索引數組 nums。

您可以對陣列套用任意次數的兩種類型的操作：

選擇兩個具有相同值的元素並將其從數組中刪除。
選擇三個具有相同值的元素並將其從陣列中刪除。
傳回使陣列為空所需的最少操作數，如果不可能，則傳回 -1。

counter後去計算是不是可以除2或除3

    """