#
# @lc app=leetcode id=385 lang=python3
#
# [385] Mini Parser
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
"""
解題思路是使用遞迴的方式來處理嵌套的列表。
首先，我們使用 eval 函數將字串轉換為列表，然後遍歷這個列表，對於每一個元素，如果它是一個整數，那麼我們直接創建一個新的 NestedInteger 並設定該值；
如果它是一個列表，那麼我們創建一個新的 NestedInteger，並遞迴調用函數來添加子元素。

"""


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        # 使用eval函數將字串轉換為列表
        return self.find(eval(s))

    def find(self, s):
        # 如果s是整數，創建一個新的 NestedInteger 並設定該值
        if type(s) == int:
            return NestedInteger(s)

        # 創建一個新的 NestedInteger
        n = NestedInteger()

        for x in s:
            # 遍歷列表s，對於每一個元素，遞迴調用find函數
            n.add(self.find(x))
        return n


"""
時間複雜度：
O(n)，其中n是字串s的長度。因為我們需要遍歷字串s的每一個元素。

空間複雜度：
O(n)。在最壞的情況下，我們需要創建n個 NestedInteger 對象。
"""
# @lc code=end
