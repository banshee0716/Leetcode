class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        
        return [len(Counter(nums[:i + 1])) - len(Counter(nums[i + 1:])) for i in range(len(nums))]
        
        """
給定一個長度為 n 的 0 索引數組 nums。

nums 的不同差異數組是長度為 n 的數組 diff，使得 diff[i] 等於後綴 nums[i + 1, ..., n - 1] 中不同元素的數量減去不同元素的數量前綴nums[0, ..., i] 中的元素。

返回 nums 的不同差異數組。

請注意，nums[i, ..., j] 表示從索引 i 開始到索引 j 結束的 nums 子數組。特別是，如果 i > j，則 nums[i, ..., j] 表示空子數組。
    """