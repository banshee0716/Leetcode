class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        records = dict()
        for index,val in enumerate(nums):
            if target-val not in records:
                records[val] = index
            else:
                return [records[target-val],index]