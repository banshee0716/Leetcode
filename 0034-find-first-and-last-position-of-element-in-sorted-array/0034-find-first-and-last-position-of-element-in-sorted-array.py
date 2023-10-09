class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #搜尋最左邊元素的binary search
        def search(x):
            low, high = 0, len(nums)
            
            while low < high:
                mid = low + (high-low) // 2
                if nums[mid] < x:
                    low = mid+1
                else:
                    high = mid
                
            return low
        
        first = search(target)
        last = search(target+1)-1
        
        if first <= last:
            return [first, last]
        else:
            return [-1, -1]
        
"""
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


"""