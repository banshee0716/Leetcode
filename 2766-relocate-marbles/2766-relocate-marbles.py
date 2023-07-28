class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        nums = set(nums)
        for frm, to in zip(moveFrom, moveTo):
            nums.remove(frm)
            nums.add(to)
        
        return sorted(nums)
        
        
"""
給你一個 0 索引的整數數組 nums ，表示一些彈珠的初始位置。您還獲得兩個長度相等的 0 索引整數數組 moveFrom 和 moveTo。

在整個 moveFrom.length 步驟中，您將更改彈珠的位置。在第 i 步中，您將把位置 moveFrom[i] 處的所有彈珠移動到位置 moveTo[i] 處。

完成所有步驟後，返回已排序的佔用位置列表。

筆記：

如果該位置至少有一顆彈珠，我們稱該位置已被佔據。
一個位置可能有多個彈珠。

time complexity is O(NKlogK)
space complexity is O(K)
"""