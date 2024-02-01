class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        
        for i in range(0, len(nums), 3):
            if nums[i+2] - nums[i] > k:
                return []
            else:
                ans.append(nums[i:i+3])
                
        return ans
                
        
    
    """
給定一個 的整數數組 nums 和一個正整數 k。

將陣列分成一個或多個大小為 3 且符合下列條件的陣列：
    -nums 的每個元素都應該位於陣列中。
    -一個數組中任兩個元素之間的差值小於或等於 k。
    
傳回包含所有數組的二維數組。如果無法滿足條件，則傳回空數組。如果有多個答案，則傳回其中任何一個。
    """