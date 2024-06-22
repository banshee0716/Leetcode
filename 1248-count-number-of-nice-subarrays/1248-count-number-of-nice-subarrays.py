class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count_odd = 0
        total_nice = 0
        cur_nice = 0
        start = 0
        
        for end in range(len(nums)):
            if nums[end] % 2:
                count_odd += 1
                cur_nice = 0
                
            while count_odd == k:
                if nums[start] % 2:
                    count_odd -= 1
                cur_nice += 1
                start += 1
            total_nice += cur_nice
            
        return total_nice
                
        