from typing import List

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        # 使用集合來存儲數字，以便於快速查找
        num_set = set(nums)
        max_k = -1
        
        # 遍歷數組
        for n in nums:
            # 如果n是正數且其相反數存在於集合中
            if n > 0 and -n in num_set:
                max_k = max(max_k, n)
        
        return max_k

            
        
"""
解題思路
1. 建立集合：利用集合來儲存nums中的所有元素，以便快速查找。
2. 遍歷數組：遍歷nums中的每個元素：
    -如果當前數字是正數，且其相反數（即-n）也在集合中，則更新目前找到的最大正數k。
    
3. 返回結果：如果找到了滿足條件的最大正數k，則返回該數字；否則，返回-1。

時間複雜度分析
時間複雜度：O(n)，其中n是nums的長度。我們遍歷nums一次，每次檢查集合的存在性操作需要O(1)時間。

空間複雜度分析
空間複雜度：O(n)，用於存儲數組元素的集合。
"""