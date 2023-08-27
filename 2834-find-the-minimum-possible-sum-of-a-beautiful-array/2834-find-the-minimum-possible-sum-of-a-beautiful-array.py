class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        seen = set()
        i = 1
        while len(seen) < n:
            if target - i not in seen:
                seen.add(i)
                
            i +=1 
            
        return sum(seen)
        
        
        """
給定正整數 n 和目標。

如果數組 nums 滿足以下條件，那麼它就是美麗的：

nums.length == n。
nums 由成對不同的正整數組成。
在 [0, n - 1] 範圍內不存在兩個不同的索引 i 和 j，因此 nums[i] + nums[j] == target。
返回一個漂亮數組可能具有的最小可能總和。
        """