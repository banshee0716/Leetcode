from itertools import accumulate

class Solution:
    def maxFrequency(self, nums, k):
        nums.sort()
        acc_sums = list(accumulate(nums))

        max_freq, visit = 1, set()

        for j in range(len(nums) - 1, 0, -1):
            # skip same value on the left
            if nums[j] not in visit:
                visit.add(nums[j])

                l, r = 0, j
                while l < r:
                    m = l + (r - l)//2

                    if acc_sums[j] - acc_sums[m] + nums[m] + k < (j - m + 1) * nums[j]:
                        l = m + 1
                    else:
                        r = m

                freq = j - l + 1

                max_freq = max(max_freq, freq)

        return max_freq