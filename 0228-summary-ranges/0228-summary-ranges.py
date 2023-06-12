class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        for n in nums:
            if not ranges or n > ranges[-1][-1] + 1:
                ranges += [],
            ranges[-1][1:] = n,

        return ["->".join(map(str, r)) for r in ranges]

"""
解題思路:

初始化一個空的範圍列表。
遍歷數組中的每個數字。
如果範圍列表為空或當前數字大於最後一個範圍的結尾加一，則添加一個新的範圍。
否則，將當前數字添加到最後一個範圍的結尾。
最後，將每個範圍轉換為字符串並返回。

時間複雜度:
O(n)，因為我們需要遍歷一次輸入的數組，其中n是數組的長度。

空間複雜度:
O(m)，我們需要儲存m個範圍，其中m是範圍的數量。在最壞的情況下，每個數字都會形成一個範圍，所以m最多可以等於n。
"""