class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = {}
        for val, index in enumerate(nums):
            if target - index in record:
                return [record[target - index], val]
            else:
                record[index] = val