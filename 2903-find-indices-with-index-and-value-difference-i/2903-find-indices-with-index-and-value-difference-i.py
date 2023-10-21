class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        if indexDifference == 0 and valueDifference == 0:
            return [0,0]
        for i in range(len(nums)-1):
            for j in range(i, len(nums)):
                if abs(i-j) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]
        return [-1, -1]
            
        
    """
給您一個具有長度為n，整數索引差和整數劃分的0個索引整數數字數字。

您的任務是在[0，n -1]範圍內找到兩個i和j的索引I和J，它們滿足以下條件：

- abs（i -j）> = indexDifference，並且
- abs（nums [i]  -  nums [j]）> = valueDifference
返回整數陣列答案，其中答案= [i，j]如果有兩個索引，則答案= [-1，-1]否則。如果兩個指數有多種選擇，請返回其中任何一個。

注意：I和J可能相等。
    """