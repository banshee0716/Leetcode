class Solution:
    #seaarch for duplicate numbers, linear search
    def numIdenticalPairs(self, nums: List[int]) -> int:
        repeat = {}
        ans = 0
        for i in nums:
            if i in repeat:
                if repeat[i] == 1:
                    ans += 1
                else:
                    ans += repeat[i]
                
                repeat[i] += 1
            else:
                repeat[i] = 1
                
        return ans