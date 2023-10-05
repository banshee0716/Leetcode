class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        element_count = Counter(nums)  
        result = []
        n = len(nums)//3
        
        for element, count in element_count.items():
            if count > n:
                result.append(element)
                
        return result
            
"""
counter計算之後把所有的值>3的全部塞進一個list裡面

Time complexity: O(N)
Since we are iterating over the array in two passes then the complexity is 2 * N which is O(N).

Space complexity: O(1)
Since we are only storing constant variables then the complexity is O(1).
"""