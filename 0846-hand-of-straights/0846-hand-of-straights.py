import collections, heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # 如果 hand 的長度不是 groupSize 的倍數，返回 False
        if len(hand) % groupSize:
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

    
"""
解題思路：
1. 首先檢查 hand 的長度是否是 groupSize 的倍數。如果不是，直接返回 False。
2. 使用 collections.defaultdict 來計算 hand 中每個數的出現次數。
3. 使用小根堆來存儲 hand 中的不同數值，便於我們從最小的開始處理。
4. 當小根堆不為空時，每次都從堆頂取出最小的數，然後檢查是否可以組成一組連續的 groupSize 大小的數組。
5. 最後，如果成功地組成了若干組大小為 groupSize 的連續數組，返回 True，否則返回 False。

時間複雜度：最壞情況是 O(nlogn)，其中 n 是 hand 的長度。這是因為我們對所有數進行了排序，並且對每個數進行了處理。
空間複雜度：O(n)，我們使用了一個字典和一個小根堆來存儲 hand 中的數。
"""