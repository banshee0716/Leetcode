class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        for i in range(1, len(chalk)):
            chalk[i] += chalk[i-1]
        
        k = k % chalk[-1]
        left, right = 0, len(chalk)
        
        while left < right:
            mid = left + (right-left) // 2
            if chalk[mid] > k:
                right = mid
            else:
                left = mid+1
                
        return left
            
        