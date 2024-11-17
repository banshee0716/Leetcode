class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefixSums = [0] * (n + 1)
        
        for i in range(n):
            prefixSums[i + 1] = prefixSums[i] + nums[i]
            
        result = n + 1
        deque_indices = deque()
        
        for i in range(n + 1):
            while deque_indices and prefixSums[i] - prefixSums[deque_indices[0]] >= k:
                result = min(result, i - deque_indices.popleft())
            while deque_indices and prefixSums[i] <= prefixSums[deque_indices[-1]]:
                deque_indices.pop()
            
            deque_indices.append(i)
            
        return result if result <= n else -1
        
        
        
        