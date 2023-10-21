class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dq = deque()
        for i in range(len(nums)):
            nums[i] += nums[dq[0]] if dq else 0
            
            while dq and (i - dq[0] >= k or nums[i] >= nums[dq[-1]]):
                dq.pop() if nums[i] >= nums[dq[-1]] else dq.popleft()
                
            if nums[i] > 0:
                dq.append(i)
                
        return max(nums)

    
"""
給定一個整數數組 nums 和一個整數 k，傳回該數組的非空子序列的最大和，使得對於子序列中的每兩個連續整數 nums[i] 和 nums[j]，
其中 i < j，滿足條件j - i <= k。

數組的子序列是從數組中刪除一定數量的元素（可以是零）而獲得的，其餘元素保留其原始順序。
"""