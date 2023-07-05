class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # 初始化最長連續 1 的長度、前一段連續 1 的長度和當前連續 1 的長度
        longest = prev = curr = 0

        # 遍歷輸入的數字列表
        for bit in nums:
            if bit:
                # 如果當前數字是 1，則增加 curr 的值
                curr += 1
                # 更新最長連續 1 的長度
                longest = max(longest, prev + curr)
            else:
                # 如果當前數字是 0，則將 curr 的值存入 prev，然後將 curr 重置為 0
                prev, curr = curr, 0

        # 如果最長連續 1 的長度等於列表的長度，則返回最長長度減 1（因為至少需要一個 0）
        # 否則直接返回最長長度
        return longest - (longest == len(nums))

    
    
"""
尋找最長的子陣列，其中每個元素至少有一個相鄰元素是 1。
解決此問題的主要思路是使用兩個變數 prev 和 curr 來記錄連續的 1 的長度，每當遇到 0 時，就將 curr 的值存入 prev，然後將 curr 重置為 0。如果遇到的是 1，則增加 curr 的值。

時間複雜度為 O(n)，因為程式碼需要遍歷一次數字列表。
空間複雜度為 O(1)，因為此程式碼只使用了固定數量的變數，並未使用與輸入大小相關的額外空間。
"""