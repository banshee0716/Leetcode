class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        
        n = len(nums) 

        # If the array has only one element, then not possible to partition into valid subarrays 
        if n == 1: 
            return False 

        # Initialization for the first three values 
        dp = [True, False, nums[0] == nums[1] if n > 1 else False] 

        for i in range(2, n): 
            current_dp = False 

            # Check for 2 equal elements 
            if nums[i] == nums[i-1] and dp[1]: 
                current_dp = True 

            # Check for 3 equal elements 
            elif nums[i] == nums[i-1] == nums[i-2] and dp[0]: 
                current_dp = True 

            # Check for 3 consecutive increasing elements 
            elif nums[i] - nums[i-1] == 1 and nums[i-1] - nums[i-2] == 1 and dp[0]: 
                current_dp = True 

            # Move the window forward 
            dp[0], dp[1], dp[2] = dp[1], dp[2], current_dp 

        return dp[2]
    
    """
給定一個 0 索引的整數數組 nums。您必須將數組劃分為一個或多個連續的子數組。

如果獲得的每個子數組滿足以下條件之一，我們稱數組的分區有效：

1. 該子數組恰好由 2 個相等的元素組成。例如，子數組 [2,2] 就很好。
2. 該子數組恰好由 3 個相等的元素組成。例如，子數組 [4,4,4] 就很好。
3. 子數組恰好由3個連續遞增元素組成，即相鄰元素之間的差為1。例如，子數組[3,4,5]是好的，但子數組[1,3,5]則不行。

如果數組至少有一個有效分區，則返回 true。否則，返回 false。
    """