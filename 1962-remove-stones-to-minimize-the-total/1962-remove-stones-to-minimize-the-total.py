class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        priority_queue = [-x for x in piles]
        heapify(priority_queue)
        for i in range(k):
            heapreplace(priority_queue, priority_queue[0] // 2 )
        
        return -sum(priority_queue)

    
    
    
    
    # You should apply the following operation exactly k times: