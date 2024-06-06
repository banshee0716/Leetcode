class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        # 使用字典來計算每個數的出現次數
        freq = collections.defaultdict(int)
        for num in hand:
            freq[num] += 1
            
        # 將所有的數放入小根堆
        min_heap = list(freq.keys())
        heapq.heapify(min_heap)
        
        # 當小根堆不為空時，每次都從堆頂取出最小的數
        while min_heap:
            smallest = min_heap[0]
            # 檢查是否可以組成一組連續的 groupSize 大小的數組
            for num in range(smallest, smallest + groupSize):
                if num not in freq:
                    return False
                freq[num] -= 1
                if freq[num] == 0:
                    if num != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)
                    
        return True

    