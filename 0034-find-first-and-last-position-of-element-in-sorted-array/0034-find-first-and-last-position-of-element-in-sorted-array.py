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
        # 一次找最左邊，另一個找下一個元素的最左邊－１＝前一個元素的最右邊
        first = search(target)
        last = search(target+1)-1
        
        if first <= last:
            return [first, last]
        else:
            return [-1, -1]
    
"""
時間複雜度分析：
我們執行了兩次二分查找，每次的時間複雜度均為 O(logn)，因此整體時間複雜度也是 O(logn)。
空間複雜度分析：
我們只使用了常數級別的額外空間，因此空間複雜度為 O(1)。
"""