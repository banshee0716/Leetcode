class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = []
        if k == 1:
            return nums[:]
        if n < k:
            return result
        diff = [nums[i + 1] - nums[i] for i in range(n - 1)]
        bad = 0
        
        for i in range(k - 1):
            if diff[i] != 1:
                bad += 1
        for i in range(n - k + 1):
            if bad == 0:
                result.append(nums[i + k - 1])
            else:
                result.append(-1)
            if i + k - 1 < n - 1:
                if diff[i] != 1:
                    bad -= 1
                if diff[i + k - 1] != 1:
                    bad += 1
            else:
                if diff[i] != 1:
                    bad -= 1
        
        return result