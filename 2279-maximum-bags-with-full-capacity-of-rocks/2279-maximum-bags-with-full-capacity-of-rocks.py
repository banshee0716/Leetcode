class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        for i in range(len(capacity)):
            capacity[i] -= rocks[i]# 算出剩餘的空含量
        
        ans = 0
        capacity.sort() # 從剩的比較少的開始填起
        while ans < len(capacity) and additionalRocks - capacity[ans] >= 0:
            additionalRocks -= capacity[ans] #開始填填看空的背包
            ans += 1 # 填完一格了
        
        return ans