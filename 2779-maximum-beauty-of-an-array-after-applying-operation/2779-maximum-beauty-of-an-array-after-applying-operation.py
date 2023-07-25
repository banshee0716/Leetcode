class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()  # sort the array
        start = 0  # start of the window
        ans = 0  # maximum length of the window
        for end in range(len(nums)):
            # if the window is not valid, increment the start of the window
            while nums[end] - nums[start] > 2 * k:
                start += 1
            # if the current window is valid, consider it
            ans = max(ans, end - start + 1)
        return ans
