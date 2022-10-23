class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = n*(n+1)//2 #等差級數公式
        miss = s-sum(set(nums))
        duplicute = sum(nums) + miss - s
        return [duplicute, miss]
        
        
        #原本的nums是一個1-n的集合，但有一個出錯了，要找到重複之處跟重複的數值