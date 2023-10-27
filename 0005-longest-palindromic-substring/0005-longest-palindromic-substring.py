class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 初始化最長回文子串為空
        res = ""
        # 計算字符串的長度
        length = len(s)
        
        # 定義擴展回文串的函數
        def helper(left: int, right: int) -> str:
            # 檢查當前left和right指向的字符是否相等
            # 並且檢查left和right是否在字符串的範圍內
            while left >= 0 and right < length and s[left] == s[right]:
                left -= 1
                right += 1
            # 返回擴展後的回文串
            return s[left + 1 : right]
        
        # 遍歷字符串中的每個字符
        for index in range(length):
            # 以當前字符為中心擴展回文串
            # 比較並更新最長的回文串
            res = max(
                helper(index, index), helper(index, index + 1), res, key=len
            )
            
        # 返回最長的回文子串
        return res
"""
解題思路：

1. 初始化一個變量res用來存儲最長的回文子串，初始值為空字符串。

2. 定義一個helper函數，這個函數接收兩個參數left和right，用於擴展以s[left]和s[right]為中心的回文串。
    -在helper函數內，使用一個while循環檢查當前left和right指向的字符是否相等，並且檢查left和right是否在字符串的範圍內。
    - 如果以上條件都滿足，則左右兩邊同時擴展，即left--，right++。
    - 最後返回擴展後的回文串。
    
3. 使用一個for循環，遍歷字符串s中的每個字符，並以當前字符為中心擴展回文串。
    -因為回文串的長度可能是奇數也可能是偶數，所以需要調用兩次helper函數：helper(index, index)和helper(index, index + 1)。
    -使用max函數更新res，key參數設為len，即比較根據字符串的長度來更新最長的回文串。
    
4. 返回res，即最長的回文子串。

時間複雜度分析：
對於每個字符，我們最多會擴展n/2次（n為字符串的長度），所以時間複雜度為O(n^2)。

空間複雜度分析：
我們只使用了常量級別的額外空間，所以空間複雜度為O(1)。




"""