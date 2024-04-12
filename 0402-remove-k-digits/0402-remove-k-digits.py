class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # If k > 0, remove remaining k digits from the end of the stack
        stack = stack[:-k] if k > 0 else stack
        
        # Remove leading zeros
        result = ''.join(stack).lstrip('0')
        
        # Handle edge case where result might be empty
        return result if result else '0'             
    """
解題思路
這個問題可以通過使用棧（Stack）來解決。具體方法如下：

遍歷給定的數字字符串，對於每一個數字：
    -當棧不為空，且還需要移除的數字個數k大於0，且棧頂的數字大於當前數字時，從棧中彈出棧頂元素，並將k減1。
    -將當前數字推入棧中。
    -最後，如果k仍然大於0，則從棧尾部移除k個元素。
將棧中剩餘的元素轉化為字符串，並去除前導零。
    
時間複雜度分析
遍歷數字字符串的時間複雜度為O(N)，其中N是數字字符串的長度。
每個數字最多被推入棧和彈出棧一次，因此總操作次數也是O(N)。
總時間複雜度為O(N)。

空間複雜度分析
使用了一個棧來存儲最終的數字，空間複雜度為O(N)。
    """