class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        
        return len(nums) < 3 or any(nums[i] + nums[i+1] >= m for i in range(len(nums)-1))
        
"""   
給定一個長度為 n 的數組 nums 和一個整數 m。您需要通過執行一系列步驟來確定是否可以將數組拆分為 n 個非空數組。

在每個步驟中，您可以選擇一個長度至少為2 的現有數組（可能是前面步驟的結果）並將其拆分為兩個子數組，前提是對於每個生成的子數組，至少滿足以下條件之一：

子數組的長度為 1，或者
子數組的元素之和大於或等於m。
如果可以將給定數組拆分為 n 個數組，則返回 true，否則返回 false。

注意：子數組是數組中連續的非空元素序列。


如果 len(nums) 是 1 或 2，那麼解決方案就是“True”。
否則，策略是從列表的 nums 的頭部或尾部逐一削減單個元素的子數組，直到我們到達包含兩個元素的剩餘子數組。
如果存在總和至少為 m 的對，則我們對該子數組進行配對，並返回 True。如果不存在這樣的對，我們返回 False。

Complexity
Time O(n)
Space O(1)
    """