# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # 初始化一個棧，並將輸入的 nestedList 反轉後放入棧中。
        # 反轉是因為我們想從 nestedList 的開始處開始遍歷，而棧的特性是先入後出。
        self.stack = nestedList[::-1]
    
    def next(self) -> int:
        # 直接彈出棧頂元素並返回其整數值。
        # 由於我們已確保棧頂元素是一個整數(在 hasNext 函數中)，所以可以直接調用 getInteger()。
        return self.stack.pop().getInteger()
    
    def hasNext(self) -> bool:
        # 當棧不為空時，持續檢查棧頂元素。
        while self.stack:
            top = self.stack[-1]  # 取得棧頂元素但不彈出
            if top.isInteger():
                # 如果棧頂元素是整數，直接返回 True
                return True
            # 如果棧頂元素是列表，則彈出棧頂元素並將其反轉後再放回棧中。
            self.stack = self.stack[:-1] + top.getList()[::-1]
            
        # 如果棧為空，表示沒有下一個元素。
        return False
"""
解題思路：

1. 我們使用一個棧來協助我們迭代巢狀列表。
2. 在 hasNext 函數中，我們檢查棧頂元素。
3. 如果它是一個整數，我們知道還有下一個元素。
4. 如果它是一個列表，我們需要將其壓平，即彈出當前的列表並將其元素反轉後再放入棧中。
時間複雜度：

假設整個巢狀列表中總共有 N 個元素(包括整數和子列表)，那麼 hasNext 和 next 函數的時間複雜度均為 O(N)。因為每個元素只會被放入和彈出棧一次。
空間複雜度：

在最壞的情況下，我們可能需要將所有的 N 個元素都放入棧中，所以空間複雜度為 O(N)。

"""
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())