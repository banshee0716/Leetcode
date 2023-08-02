class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 儲存所有可能組合的列表
        ans = []
        # 從空數組開始選取
        self.helper(nums, [], ans)
        return ans
    
    def helper(self, nums, temp, ans):
        # 如果數組為空，則當前組合為一種可能組合
        if len(nums) == 0:
            ans.append(temp)
            return 
        # 遍歷數組中的每個數字
        for i in range(len(nums)):
            # 選取當前數字，並在剩餘數組中繼續選取
            self.helper(nums[:i]+nums[i+1:], temp+[nums[i]], ans)
