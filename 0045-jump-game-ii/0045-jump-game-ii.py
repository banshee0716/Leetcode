class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        l, r = 0, nums[0]
        res = 1
        while r<len(nums)-1:
            res += 1
            nxt = max(i + nums[i] for i in range(l, r + 1))
            l, r = r, nxt
        return res
        
#In other words, if you are at nums[i], you can jump to any nums[i + j] where:

#0 <= j <= nums[i] and
#i + j < n