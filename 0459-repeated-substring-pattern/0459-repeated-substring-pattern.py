class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # 檢查s是否存在於s[1:] + s[:-1]中
        return s in s[1:] + s[:-1]

"""
解題思路如下：

假設原字串s可以由某個子字串pattern重複k次組成，即s = pattern * k。現在，我們考慮新的字串s2 = s + s，那麼s2的內容就是s兩次相接，即s2 = s * 2。但pattern * k = s，所以s2 = pattern * 2k。

現在，我們從s2中刪除第一個和最後一個字符，得到s2'，即s2' = s[1:] + s[:-1]。在這個新的字串s2'中，如果s出現，那麼s就可以由子字串pattern重複多次組成。

時間複雜度: 
O(n)，其中n是s的長度。這是因為s[1:] + s[:-1]的操作是O(n)，而s是否存在於此新的字串中的查找操作也是O(n)。

空間複雜度:
O(n)。新的字串s[1:] + s[:-1]會佔用O(n)的空間。
"""