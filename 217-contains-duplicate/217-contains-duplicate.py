class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        exist_set = set()
        for i in nums:
            if i not in exist_set:
                exist_set.add(i)
            else:
                return True
        
        return False