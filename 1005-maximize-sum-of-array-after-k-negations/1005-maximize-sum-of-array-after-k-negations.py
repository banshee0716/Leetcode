from typing import List

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # 首先對列表進行升序排序
        nums = sorted(nums)
        
        # 遍歷整數列表，將負數變為正，最多操作 k 次
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1
        
        # 再次進行升序排序
        nums = sorted(nums)
        
        # 如果 k 是奇數，則將最小的整數變為其反數
        if k > 0 and k % 2 != 0:
            nums[0] = -nums[0]
        
        # 返回列表的總和
        return sum(nums)
    
"""
1. 首先將整數列表進行升序排序，這樣我們就可以從最小的整數開始，因為把負數變為正數會增加列表的總和。
2. 遍歷排序後的列表，如果當前的整數是負的且 k 大於0，則將其改為正，並將 k 減1。
3. 再次將列表進行升序排序。此時，我們需要考慮 k 的值，如果 k 還有剩餘，且 k 是奇數，則反轉列表中的最小整數。因為只有當 k 是奇數時，總和會被影響。
4. 最後，返回列表的總和。


時間複雜度: 
主要是排序操作，所以為 O(nlogn)，其中 n 是 nums 的長度。

空間複雜度:
O(1)，因為我們只使用了常數的額外空間。
"""