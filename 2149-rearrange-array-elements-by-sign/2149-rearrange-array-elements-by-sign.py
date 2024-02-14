class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        pos, neg = 0, 1
        for num in nums:
            if num > 0:
                ans[pos] = num
                pos += 2
                
            else:
                ans[neg] = num
                neg += 2
        
        return ans
        
        
    
    """
給定一個偶數長度的 0 索引整數數組 nums，由相等數量的正整數和負整數組成。

您應該重新排列 nums 的元素，以便修改後的陣列遵循給定的條件：
1. 每對連續的整數都有相反的符號。
2. 對於所有具有相同符號的整數，它們在 nums 中出現的順序將被保留。
3. 重新排列的陣列以正整數開頭。

重新排列元素以滿足上述條件後，傳回修改後的陣列。
    """