class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s1, s2, s3 = set(nums1), set(nums2), set(nums3)
        return s1 & s2 | s2 & s3 | s1 & s3 
        
"""
給定三個整數數組 nums1、nums2 和 nums3，返回一個不同的數組，其中包含三個數組中至少兩個數組中存在的所有值。您可以按任何順序返回值。
"""