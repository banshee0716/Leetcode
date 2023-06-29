class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        
        start = total = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                start = i+1
        
        return start
            
        

"""
找一個起始點，從那邊開始greedy，只要整個過程中的gas-cost都大於0，那就可以通過了
"""