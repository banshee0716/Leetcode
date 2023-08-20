class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        ans = ""
        for word in words:
            ans += word[0]
        return ans == s
        
        
        """
給定一個字符串數組 Words 和一個字符串 s，確定 s 是否是單詞的首字母縮略詞。

如果字符串 s 可以通過按順序連接單詞中每個字符串的第一個字符來形成，則該字符串 s 被視為單詞的首字母縮略詞。例如，“ab”可以由 [“apple”, “banana”] 組成，但不能由 [“bear”, “aardvark”] 組成。

如果 s 是單詞的首字母縮寫詞，則返回 true，否則返回 false。
        """