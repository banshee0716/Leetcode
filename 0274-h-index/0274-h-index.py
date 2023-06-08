class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)  # 將引用次數由高至低排序
        n, h = len(citations), 0  # n為論文數量，h為H指數
        for i in range(n):  # 遍歷每篇論文
            if citations[i] >= i+1:  # 若當前論文的引用次數大於等於其排序位置（即至少有i+1篇論文被引用了i+1次）
                h += 1  # H指數加一
            else:  # 若當前論文的引用次數小於其排序位置，則停止遍歷
                break
        return h  # 回傳H指數
"""
解題思路:
先將引用次數由高至低排序，然後遍歷每篇論文，若該論文的引用次數大於等於其排序位置（即至少有i+1篇論文被引用了i+1次），則H指數加一，否則停止遍歷，最後回傳H指數。

時間複雜度:
O(nlogn) - 因為要先對引用次數進行排序，所以時間複雜度是 O(nlogn)。

空間複雜度:
O(1) - 這個演算法只使用了常數的額外空間。
"""