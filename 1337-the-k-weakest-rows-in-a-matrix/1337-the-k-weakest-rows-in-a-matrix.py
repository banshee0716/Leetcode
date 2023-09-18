import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for i, row in enumerate(mat):
            strength = sum(row)
            heappush(heap, (-strength, -i))
            if len(heap) > k:
                heappop(heap)
        
        return [-i for _, i in sorted(heap, reverse=True)]
    
        #用minheap去處理，之後再來想要怎麼計算出每一行的參數（Sum()函數）