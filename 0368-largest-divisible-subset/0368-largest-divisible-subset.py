class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n
        max_size, max_index = 1, 0
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j]+1)
                    if dp[i] > max_size:
                        max_size = dp[i]
                        max_index = i
                        
        result = []
        num = nums[max_index]
        for i in range(max_index, -1, -1):
            if num % nums[i] == 0 and dp[i] == max_size:
                result.append(nums[i])
                num = nums[i]
                max_size -= 1
                
        return result
        
        
    """
給定一組不同的正整數 nums，傳回最大子集答案，使得該子集中的每對 (answer[i],answer[j]) 元素滿足：

答案[i] % 答案[j] == 0，或者
答案[j] % 答案[i] == 0
如果有多個解決方案，則傳回其中任何一個。
    """