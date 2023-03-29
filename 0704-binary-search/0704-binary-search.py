class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r: 
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            else: 
                r = mid
        return l if nums[l] == target else -1
    
    
    '''
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right-left) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return left if nums[left] == target else -1'''