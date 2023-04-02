class Solution:
    def hIndex(self, citations):
        if not citations: 
            return 0
        n = len(citations)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right)//2
            if mid + citations[mid] >= n:
                right = mid - 1
            else:
                left = mid + 1                
        return n - left