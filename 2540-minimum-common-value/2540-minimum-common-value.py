class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        common = float('inf')

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                common = nums1[i]
                return common
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
                
        return -1
                
        
        
    
    
    """
給定兩個整數陣列 nums1 和 nums2，按非遞減順序排序，傳回兩個陣列共有的最小整數。如果 nums1 和 nums2 之間沒有公共整數，則傳回 -1。

請注意，如果 nums1 和 nums2 數組中至少出現一次該整數，則稱該整數為 nums1 和 nums2 所共有。
    """