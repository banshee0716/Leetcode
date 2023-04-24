class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i, stone in enumerate(stones):
            stones[i] = -stone
        heapify(stones)
        while len(stones) > 1:
            stone1 = -heappop(stones)
            stone2 = -heappop(stones)
            if stone1 > stone2:
                heappush(stones, stone2 - stone1)
                
        return -heappop(stones) if len(stones) else 0

