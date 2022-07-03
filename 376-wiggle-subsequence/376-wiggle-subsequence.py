class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = 1
        up = None #檢測現在是不是有變化
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1] and up != True:
                up = True
                length += 1
            if nums[i] < nums[i-1] and up != False:
                up = False
                length += 1
                
        return length
        
        # i跟i+1的數值在正負之間反覆變化