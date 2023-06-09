#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)  # 從大排到小
        n, h = len(citations), 0
        for i in range(n):
            if citations[i] >= i + 1:  # 如果i比i+1大就把h+1，然後其實就可以break節省迴圈剩餘次數
                h = i + 1
            else:
                break
        return h


"""將被引用的文章按照引用次數排序，引用次數高的排在最前面，引用次數少的排在最後，
從排序的結果可看出被引用的文章「有h篇文章至少被引用h次」。"""
# @lc code=end
