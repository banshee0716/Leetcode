class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return max(dp)
    
    """
你是一名職業強盜，計劃搶劫街上的房屋。每棟房子都藏有一定數量的錢，唯一阻止你搶劫的限制是相鄰的房子都有安全系統連接，如果相鄰的兩棟房子在同一天晚上被闖入，它會自動聯繫警方。

給定一個表示每棟房子的金額的整數數組 nums，返回今晚您可以在不報警的情況下搶劫的最大金額。
    """