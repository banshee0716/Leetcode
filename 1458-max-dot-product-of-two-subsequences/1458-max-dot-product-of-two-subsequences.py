class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [-math.inf] * (m + 1)
        for i in range(1, n + 1):
            dp, old_dp = [-math.inf], dp
            for j in range(1, m + 1):
                dp += max(
                    old_dp[j], # not select i
                    dp[-1], # not select j
                    old_dp[j - 1], # not select either
                    max(old_dp[j - 1], 0) + nums1[i - 1] * nums2[j - 1], # select both
                ),
        return dp[-1]     