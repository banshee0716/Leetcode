class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(x):
            low,high=0,len(nums)
            while low < high:
                mid = (low + high) // 2
                if nums[mid] < x:
                    low = mid + 1
                else:
                    high = mid
            
            return low
        
        low = search(target)
        high = search(target+1)-1
        
        if (low <= high):
            return [low,high]
        else:
            return [-1,-1]